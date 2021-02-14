import time

import jwt
from django.conf import settings


def make_token(username, exp=3600 * 24):
    key = settings.JWT_TOKEN_KEY
    payload = {'username': username, 'exp': time.time() + exp}
    return jwt.encode(payload, key, algorithm='HS256')
