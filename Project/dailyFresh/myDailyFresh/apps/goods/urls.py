
from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from . import views
from .views import IndexView

urlpatterns = [
    # path('', IndexView.as_view(), name='index'),  # 首页
    path('index/', IndexView.as_view(), name='index'),  # 首页

]
