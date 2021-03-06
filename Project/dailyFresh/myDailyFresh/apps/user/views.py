from django.conf import settings
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.shortcuts import render, redirect
import re
from django.core.mail import send_mail
from django.urls import reverse
from django.views import View
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from celery_tasks.task import send_register_active_email

from .models import User


# Create your views here.
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
    send_register_active_email.delay(email,username,token)
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
    return redirect(reverse('index'))


class ActiveView(View):
    """用户激活"""

    def get(self, request, token):
        # 解密参数
        serializer = Serializer(settings.SECRET_KEY, 3600*2)
        try:
            info = serializer.loads(token.encode())
            user_id = info['confirm']

            # 根据id获取用户id
            user = User.objects.get(id=user_id)
            user.is_active = 1
            user.save()
            # 跳转登录
            print(reverse('login'))
            return redirect(reverse('login'))

        except Exception as e :
            # 激活链接已过期
            print(e)
            return HttpResponse('激活链接已过期')


class LoginView(View):
    def get(self, request):
        return render(request, 'login.html')
    def post(self,request):
        # 接收数据
        username = request.POST.get('username')
        password = request.POST.get('pwd')

        # 校验数据
        if not all([username, password]):
            return render(request, 'login.html', {'errmsg': '数据不完整'})

        # 业务处理
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                # 记录登陆状态 session
                login(request,user)
                # 跳转到首页

                return redirect(reverse('index'))
            else:
                return render(request, 'login.html', {'errmsg': '账户未激活'})

        else:
            return render(request, 'login.html', {'errmsg': '用户名或密码错误'})