import jwt
from django.http import HttpResponse
from rest_framework.authentication import get_authorization_header, BaseAuthentication
from rest_framework import exceptions

from dashboard.models import User


class TokenAuthentication(BaseAuthentication):
    model = None

    def get_model(self):
        return User

    def authenticate(self, request):
        print('entered')
        auth = get_authorization_header(request).split()
        print(auth)
        if not auth or auth[0].lower() != b'jwt':
            return None
        print(auth[1])
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
        model = self.get_model()
        payload = jwt.decode(token, "SECRET")
        username = payload['username']
        userid = payload['user_id']
        msg = {'Error': "Token mismatch", 'status': "401"}
        try:

            user = User.objects.get(
                username=username,
                id=userid
            )

            #if not user.token['token'] ==:
             #   raise exceptions.AuthenticationFailed(msg)

        except jwt.ExpiredSignature or jwt.DecodeError or jwt.InvalidTokenError:
            print("expired")
            return HttpResponse({'Error': "Token is invalid"}, status="403")
        except User.DoesNotExist:
            print("does not exist")
            return HttpResponse({'Error': "Internal server error"}, status="500")

        return user, token

    def authenticate_header(self, request):
        return 'Token'