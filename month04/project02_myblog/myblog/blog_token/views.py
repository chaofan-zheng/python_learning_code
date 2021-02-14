import hashlib
import json

from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from django.views import View

from tools.make_token import make_token
from user.models import UserProfile


class TokenView(View):
    def post(self, request):
        json_str = request.body
        json_obj = json.loads(json_str)
        username = json_obj['username']
        password = json_obj['password']
        user = UserProfile.objects.filter(username=username)[0]
        if not user:
            return JsonResponse({'code': '10001', 'error': '用户名或密码错误'})
        md5 = hashlib.md5()
        md5.update(password.encode())
        password_h = md5.hexdigest()
        if password_h != user.password:
            return JsonResponse({'code': '10001', 'error': '用户名或密码错误'})
        token = make_token(username)
        return JsonResponse({'code': 200, 'username': username,
                             'data': {'token': token}})
