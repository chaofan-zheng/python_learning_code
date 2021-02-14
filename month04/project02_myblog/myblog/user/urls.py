from django.urls import path
from . import views
urlpatterns = [
    path('test_request',views.test_request),
    path('sms',views.sms_views),
    path('<str:username>',views.UserView.as_view()),
    path('<str:username>/avatar',views.avatar_upload),
]
