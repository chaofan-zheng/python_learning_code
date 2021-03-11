from goods.models import GoodsSKU
from django.conf import settings
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect
import re
from django.core.mail import send_mail
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views import View
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from celery_tasks.task import send_register_active_email
from django_redis import get_redis_connection

from .models import User, Address





def register(request):
    if request.method == 'GET':
        return render(request, 'register.html')
    elif request.method == 'POST':
        return register_handle(request)


def register_handle(request):
    username = request.POST.get('user_name')
    password = request.POST.get('pwd')
    email = request.POST.get('email')
    allow = request.POST.get('allow')

    # 校验
    if not all([username, password, email]):
        return render(request, 'register.html', {'errmsg': '数据不完整'})
    if allow != 'on':
        return render(request, 'register.html', {'errmsg': '请同意协议'})
    # 判断用户名是否存在
    try:
        user = User.objects.get(username=username)
    except:
        user = None
    if user:
        return render(request, 'register.html', {'errmsg': '用户名已经被注册'})
    user = User.objects.create_user(username, email, password)
    user.is_active = 0  # 刚注册的时候不能是激活的
    user.save()
    # 发送激活邮件，包含激活连接：
    # 激活连接中需要包含用户的身份信息：
    # http://127.0.0.1:8000/user/active/1
    # 1是用户id
    # 激活连接中需要包含用户的身份信息，并且要把身份信息进行加密
    # 加密使用itsdangerous包,也可以使用jwt
    serializer = Serializer(settings.SECRET_KEY, 3600 * 2)  # 两小时内过期
    info = {'confirm': user.id}
    token = serializer.dumps(info)
    token = token.decode()
    # 发邮件
    send_register_active_email.delay(email, username, token)
    # subject = '天天生鲜欢迎信息'  # 邮件标题
    # message = '' # 邮件正文
    # html_message = '<h1>%s, 欢迎成为天天生鲜注册会员<h1>' \
    #                '请点击下面链接激活账户<br/>' \
    #                '<a href="http://127.0.0.1:8000/user/active/%s">' \
    #                'http://127.0.0.1:8000/user/active/%s</a>' % (username, token, token) # 邮件正文
    # sender = settings.EMAIL_FROM  # 发送人
    # receiver = [email]  # 收件人列表
    # send_mail(subject, message, sender, receiver,html_message=html_message)
    # print(reverse('index'))
    return redirect(reverse('goods:index'))


class ActiveView(View):
    """用户激活"""

    def get(self, request, token):
        # 解密参数
        serializer = Serializer(settings.SECRET_KEY, 3600 * 2)
        try:
            info = serializer.loads(token.encode())
            user_id = info['confirm']

            # 根据id获取用户id
            user = User.objects.get(id=user_id)
            user.is_active = 1
            user.save()
            # 跳转登录
            print(reverse('user:login'))
            return redirect(reverse('user:login'))

        except Exception as e:
            # 激活链接已过期
            print(e)
            return HttpResponse('激活链接已过期')


class LoginView(View):
    def get(self, request):
        # 判断是否记住了用户名
        if 'username' in request.COOKIES:
            username = request.COOKIES.get('username')
            checked = 'checked'
        else:
            username = ''
            checked = ''
        return render(request, 'login.html', {'username': username, 'checked': checked})

    def post(self, request):
        # 接收数据
        username = request.POST.get('username')
        password = request.POST.get('pwd')

        # 校验数据
        if not all([username, password]):
            return render(request, 'login.html', {'errmsg': '数据不完整'})

        # 业务处理
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                # 记录登陆状态 session
                # login 使用Django的session框架，来将用户的ID保存在session中
                # session默认保存到django_session的mysql数据库里面
                # 因为读取速度慢，所以我们使用redis存储session
                login(request, user)
                # 获取要跳转的地址
                next_url = request.GET.get('next', reverse('goods:index'))  # 后面的是get函数的默认缺省值
                # 默认跳转到首页
                resp = redirect(next_url)
                # 判断是否需要记住用户名
                remember = request.POST.get('remember')
                if remember == 'on':
                    resp.set_cookie('username', username, max_age=7 * 24 * 3600)
                else:
                    resp.delete_cookie('username')
                return resp
            # 跳转到首页
            else:
                return render(request, 'login.html', {'errmsg': '账户未激活'})

        else:
            return render(request, 'login.html', {'errmsg': '用户名或密码错误'})


class LogoutView(View):
    def get(self, request):
        logout(request)
        #  跳转到首页
        return redirect(reverse('goods:index'))


# /user
class UserInfoView(View):
    def get(self, request):
        # 获取用户的个人信息
        user = request.user
        address = Address.objects.get_default_address(user=user)
        # 获取用户的历史浏览记录
        # import redis
        # r = redis.Redis(host='localhost',port='6379',db=1)
        con = get_redis_connection('default')
        history_key = f'history:{user.id}'
        # 获取用户最新浏览的五个商品的id
        sku_ids = con.lrange(history_key, 0, 4)
        # goods_li = GoodsSKU.objects.filter(id_in=sku_ids)# 查询谓词
        # goods_res = []
        # for a_id in sku_ids:
        #     for b_id in goods_li:
        #         if a_id == goods_li:
        #             goods_res.append(b_id)
        goods_li = []
        for id in sku_ids:
            good = GoodsSKU.objects.get(id=id)
            goods_li.append(good)
        context = {'page': 'user', 'address': address, 'goods_li': goods_li}
        return render(request, 'user_center_info.html',context )


# /user/order
class UserOrderView(View):
    def get(self, request):
        # 获取用户的全部订单信息
        return render(request, 'user_center_order.html', {'page': 'order'})


# user/address
class AddressView(View):
    def get(self, request):
        # 获取用户的默认收货地址
        user = request.user
        # try:
        #     address = Address.objects.get(user=user, is_default=True)
        # except:
        #     address = None
        address = Address.objects.get_all_address(user)
        return render(request, 'user_center_site.html', {'page': 'address', 'address': address})

    def post(self, request):
        # 接受
        receiver = request.POST.get('receiver')
        addr = request.POST.get('addr')
        zip_code = request.POST.get('zip_code')
        phone = request.POST.get('phone')
        # 校验
        if not all([receiver, addr, phone]):  # 邮编可以不传
            return render(request, 'user_center_site.html', {'errmsg': '数据不完整'})
        if not re.match(r'^1[3456789]d{9}$', phone):
            return render(request, 'user_center_site.html', {'errmsg': '手机格式不正确'})
        # 业务处理：地址添加
        # 如果用户已存在默认收货地址，添加的地址不作为默认收货地址，否则为默认收货地址
        user = request.user
        # try:
        #     address = Address.objects.get(user=user, is_default=True)
        # except:
        #     address = None
        address = Address.objects.get_default_address(user)
        if address:
            is_default = False
        else:
            is_default = True
        Address.objects.create(user=user, addr=addr, receiver=receiver, zip_code=zip_code, is_default=is_default,
                               phone=phone)
        # 返回地址页面
        return redirect(reverse('user:address'))
