from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from . import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('register', views.register, name='register'),
    # path('register_handle', views.register_handle,name='register_handle'),
    path('active/<str:token>', views.ActiveView.as_view(), name='active'),
    path('login', views.LoginView.as_view(), name='login'),
    path('logout', views.LogoutView.as_view(), name='logout'),
    path('', login_required(views.UserInfoView.as_view()), name='user'),
    path('order', login_required(views.UserOrderView.as_view()), name='order'),
    path('address', login_required(views.AddressView.as_view()), name='address'),

]
