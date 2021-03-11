from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.urls import reverse
from django_redis import get_redis_connection
from django.core.cache import cache
from goods.models import *
from order.models import OrderGoods
from django.views.generic import View


# Create your views here.
# 127.0.0.1:8000/
# def index(request):
#     """显示首页"""
#     return render(request, 'index.html')

class IndexView(View):
    def get(self, request):
        # 获取商品的种类信息
        types = GoodsType.objects.all() # 猪牛羊肉 # 新鲜水产之类
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

        # 获取用户购物车中商品的数目
        user = request.user
        cart_count = 0
        if user.is_authenticated:
            # 用户已登录
            conn = get_redis_connection('default')
            cart_key = 'cart_%d' % user.id
            cart_count = conn.hlen(cart_key)

        # 组织模板上下文
        context = {'types': types,
                   'goods_banners': goods_banners,
                   'promotion_banners': promotion_banners,
                   'cart_count':cart_count,}

        # 使用模板
        return render(request, 'index.html', context)


