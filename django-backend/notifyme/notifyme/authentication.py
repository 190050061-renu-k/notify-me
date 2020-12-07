import jwt
from django.http import HttpResponse, JsonResponse
from rest_framework.authentication import get_authorization_header, BaseAuthentication
from rest_framework import exceptions
from .settings import SECRET_KEY

from dashboard.models import User


class TokenAuthentication(BaseAuthentication):
    model = None

    def get_model(self):
        return User

    def authenticate(self, request):
        auth = get_authorization_header(request).split()
        if not auth or auth[0].lower() != b'bearer':
            return None
        if len(auth) == 1:
            msg = 'Invalid token header. No credentials provided.'
            raise exceptions.AuthenticationFailed(msg)
        elif len(auth) > 2:
            msg = 'Invalid token header'
            raise exceptions.AuthenticationFailed(msg)

        try:
            token = auth[1]
            if token == "null":
                msg = 'Null token not allowed'
                raise exceptions.AuthenticationFailed(msg)
        except UnicodeError:
            msg = 'Invalid token header. Token string should not contain invalid characters.'
            raise exceptions.AuthenticationFailed(msg)

        return self.authenticate_credentials(token)

    def authenticate_credentials(self, token):
        #model = self.get_model()
        try:
            payload = jwt.decode(token, SECRET_KEY, verify=False)
            username = payload['username']
            userid = payload['user_id']
            msg = {'Error': "Token mismatch", 'status': "401"}


            user = User.objects.get(
                username=username,
                id=userid
            )

            #if not user.token['token'] ==token:
             #   raise exceptions.AuthenticationFailed(msg)

        except jwt.ExpiredSignature or jwt.DecodeError or jwt.InvalidTokenError:
            print("expired")
            return JsonResponse({'Error': "Token is invalid"}, status="403")
        except User.DoesNotExist:
            print("does not exist")
            return HttpResponse({'Error': "Internal server error"}, status="500")

        return user, token

    def authenticate_header(self, request):
        return 'Token'


from django.contrib.auth.backends import ModelBackend


class AuthenticationBackend(ModelBackend):

    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            user = User(username=username)
            user.is_staff = True
            user.save()
        return user

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None