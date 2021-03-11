import django
from celery import Celery
import os

from django.shortcuts import render

# broker和worker在不同机子上则需要加上本段代码
# 注意，这个一定要写在django初始化的下方
# 创建一个Celery类的实例对象
from django.conf import settings
from django.core.mail import send_mail

from goods.models import GoodsType, IndexGoodsBanner, IndexTypeGoodsBanner, IndexPromotionBanner
from django.template import loader

app = Celery('celery_tasks.tasks', broker='redis://172.16.246.130:6379/2')


# 创建中间人

# 定义发邮件的函数
@app.task  # 将处理任务的方法告诉中间人
def send_register_active_email(to_email, username, token):
    subject = '天天生鲜欢迎信息'  # 邮件标题
    message = ''  # 邮件正文
    html_message = '<h1>%s, 欢迎成为天天生鲜注册会员<h1>' \
                   '请点击下面链接激活账户<br/>' \
                   '<a href="http://127.0.0.1:8000/user/active/%s">' \
                   'http://127.0.0.1:8000/user/active/%s</a>' % (username, token, token)  # 邮件正文
    sender = settings.EMAIL_FROM  # 发送人
    receiver = [to_email]  # 收件人列表
    send_mail(subject, message, sender, receiver, html_message=html_message)


@app.task
def generate_static_index_html():
    """产生首页静态页面"""
    types = GoodsType.objects.all()  # 猪牛羊肉 # 新鲜水产之类
    # 获取首页轮播商品信息
    goods_banners = IndexGoodsBanner.objects.all().order_by('index')
    # 获取首页促销活动信息
    promotion_banners = IndexPromotionBanner.objects.all().order_by('index')
    # 获取首页分类商品展示信息
    for type in types:  # GoodsType
        # 获取type种类首页分类商品的图片展示信息 根据type生成列表
        image_banners = IndexTypeGoodsBanner.objects.filter(type=type, display_type=1).order_by('index')
        # 获取type种类首页分类商品的文字展示信息
        title_banners = IndexTypeGoodsBanner.objects.filter(type=type, display_type=0).order_by('index')

        # 动态给type增:加属性，分别保存首页分类商品的图片展示信息和文字展示信息
        type.image_banners = image_banners
        type.title_banners = title_banners

    # 组织模板上下文
    #     context = {'types': types,
    #                'goods_banners': goods_banners,
    #                'promotion_banners': promotion_banners,
    # }
    # 不使用request的方法

    # 使用模板
    # 加载模版文件
    temp = loader.get_template('static_index.html')
    # 定义模版上下文
    context = {'types': types,
               'goods_banners': goods_banners,
               'promotion_banners': promotion_banners,
               }
    # 模版渲染
    static_index_html = temp.render(context)
    # 生成首页对应静态文件
    save_path = os.path.join(settings.BASE_DIR, 'static/index.html')
    with open(save_path, 'w') as f:
        f.write(static_index_html)

    # return render(request, 'index.html', context)
    # 因为index对登录用户进行了验证，但是我们用celery就是想做不登录的情况快速响应，所以就要新做一个html
