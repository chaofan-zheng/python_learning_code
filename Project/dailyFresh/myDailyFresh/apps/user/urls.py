from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('register', views.register,name='register'),
    # path('register_handle', views.register_handle,name='register_handle'),
    path('active/<str:token>',views.ActiveView.as_view(),name = 'active'),
    path('login',views.LoginView.as_view(),name='login'),


]
