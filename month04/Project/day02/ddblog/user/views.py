from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
import json
# Create your views here.
from django.views import View
from .models import UserProfile


class UserView(View):
    # 这里面的名字必须与请求方法一样。
    # 在as_view()里针对不同请求方式，在试图类中去查找对应的类的方法（封装在django里面）找到调用，没找到直接报异常
    # 异常码405 请求的方法不存在
    def get(self, request):
        return HttpResponse('--user get--')

    def post(self, request):
        # 1. 获取前段给后端的json串
        json_str = request.body
        # 2. 把json串反序列化为对象
        json_obj = json.loads(json_str)
        # 3. 从对象【字典】中获取数据
        username = json_obj['username']
        email = json_obj['email']
        phone = json_obj['phone']
        password_1 = json_obj['password_1']
        password_2 = json_obj['password_2']
        # 4. 数据检查
        # 4.1 检查数据的用户名是否可以用
        old_user = UserProfile.objects.filter(username=username)
        if old_user:
            result = {'code': 10100, 'error': '用户名已注册'}
            return JsonResponse(result)
        # 4.2 两次密码是否一致
        if password_1 != password_2:
            result = {'code': 10101, 'error': '两次密码不一致'}
        # 4.3 添加密码哈希值

        # 4.4 数据入库
        # 在高并发情况下仍然需要try

        return JsonResponse({'code': 200})
