import json

from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from django.views import View

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
        # 检查名字是否重复
        old_user = UserProfile.objects.filter(username=username)
        if old_user:
            result = {'code': 10100, 'error': '用户名已注册'}
            return JsonResponse(result)
        # 检查两次密码是否一致
        if password_1 != password_2:
            result = {'code': 10101, 'error': '两次密码不一致'}
            return JsonResponse(result)
        print(username,email,phone,password_1,password_2)