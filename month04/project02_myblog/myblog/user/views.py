import hashlib
import json
import random

from django.conf import settings
from django.core.cache import cache
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views import View

from tools.make_token import make_token
from tools.sms import YunTongXin
from user.models import UserProfile


class UserView(View):
    def post(self, request):
        json_str = request.body
        json_obj = json.loads(json_str)
        username = json_obj['username']
        email = json_obj['email']
        phone = json_obj['phone']
        password_1 = json_obj['password_1']
        password_2 = json_obj['password_2']
        sms_num = json_obj['sms_num']
        cache_key = f'sms_{phone}'
        code = cache.get(cache_key)
        # 检查 验证码是否一致
        if not code:
            result = {'code': 10110, "error": "验证码已失效"}
            return JsonResponse(result)
        if int(sms_num) != code:
            result = {'code': 10111, 'error': '验证码不一致'}
            return JsonResponse(result)
        # 检查名字是否重复
        old_user = UserProfile.objects.filter(username=username)
        if old_user:
            result = {'code': 10100, 'error': '用户名已注册'}
            return JsonResponse(result)
        # 检查两次密码是否一致
        if password_1 != password_2:
            result = {'code': 10101, 'error': '两次密码不一致'}
            return JsonResponse(result)
        # print(username, email, phone, password_1, password_2)
        md5 = hashlib.md5()
        md5.update(password_1.encode())
        password_h = md5.hexdigest()
        try:
            user = UserProfile.objects.create(username=username, password=password_h, email=email, phone=phone,
                                              nickname=username)
        except:
            result = {'code': 10102, 'error': '用户名已注册'}
            return JsonResponse(result)
        token = make_token(username)
        return JsonResponse({'code': 200, 'username': username,
                             'data': {'token': token}})

    def get(self, request):
        pass


def send_sms(phone, code):
    yuntongxin = YunTongXin(accountSid=settings.ACCOUNT_ID, accountToken=settings.AUTH_TOKEN,
                            appId=settings.APPID, templateId=settings.TEMPLATE_ID)
    yuntongxin.run(phone, code)


def sms_views(request):
    json_str = request.body
    json_obj = json.loads(json_str)
    phone = json_obj['phone']
    code = random.randint(100000, 999999)
    cache_key = f'sms_{phone}'
    cache.set(cache_key, code, 180)
    send_sms(phone, code)
    return JsonResponse({'code': 200})
