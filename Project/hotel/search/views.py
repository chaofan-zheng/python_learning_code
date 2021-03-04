import json

from django.http import JsonResponse, HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views import View


class SearchView(View):
    def get(self,request):
        pass
    def post(self, request):
        json_str = request.body
        json_obj = json.loads(json_str)
        # 从字典中获取数据
        hotelArea = json_obj['hotelArea']
        roomType = json_obj['roomType']
        amount = json_obj['amount']
        print(hotelArea,roomType,amount)

        return HttpResponse(hotelArea)
