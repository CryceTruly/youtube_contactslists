from rest_framework import authentication
import jwt
from django.conf import settings
from rest_framework import exceptions
from django.contrib.auth.models import User


class JWTAuthentication(authentication.BaseAuthentication):
    def authenticate(self, request):
        auth_data = authentication.get_authorization_header(request)
        if not auth_data:
            return None
        prefix, token = auth_data.decode('utf-8').split(' ')

        try:
            payload = jwt.decode(token, settings.JWT_SECRET)
            user = User.objects.get(username=payload['username'])
            return (user, token)
        except jwt.DecodeError:
            raise exceptions.AuthenticationFailed(
                "Your token is invalid,please login.")

        except jwt.ExpiredSignatureError:
            raise exceptions.AuthenticationFailed(
                "Your token expired,please login again.")
        return super().authenticate(request)

