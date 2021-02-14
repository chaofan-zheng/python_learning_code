from django.urls import path
from . import views
urlpatterns = [
    path('sms',views.sms_views),
    path('<str:username>',views.UserView.as_view())
]
