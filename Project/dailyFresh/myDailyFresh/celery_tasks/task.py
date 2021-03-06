import django
from celery import Celery

# 创建一个Celery类的实例对象
from django.conf import settings
from django.core.mail import send_mail
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myDailyFresh.settings')
django.setup()

app = Celery('celery_tasks.tasks', broker='redis://127.0.0.1:6379/2')
# 创建中间人

# 定义发邮件的函数
@app.task # 将处理任务的方法告诉中间人
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
