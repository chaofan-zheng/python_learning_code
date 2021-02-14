import jwt
from django.conf import settings
from django.http import JsonResponse

from user.models import UserProfile


def login_check(func):
    def wrappper(request, *args, **kwargs):
        token = request.META.get('HTTP_AUTHORIZATION')
        print(token)
        if not token:
            return JsonResponse({'code': '10301', 'error': 'please log in'})

        try:
            # decode方法中，首先会验签，签名是否有效；
            # 验签通过后，从 payload获取有效期，判断token是否在有效期内
            payload = jwt.decode(token,
                                 settings.JWT_TOKEN_KEY,
                                 algorithms=['HS256'])
        except Exception as e:
            print(e)
            result = {'code': 403, 'error': '请登录！'}
            return JsonResponse(result)
        username = payload['username']
        user = UserProfile.objects.get(username=username)
        request.myuser = user
        return func(request,*args, **kwargs)

    return wrappper
