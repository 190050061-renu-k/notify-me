import jwt
from django.contrib.auth import user_logged_in
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework_jwt.serializers import jwt_payload_handler
from dashboard.models import User
from . import settings



@api_view(['POST'])
@permission_classes([AllowAny, ])
def authenticate_user(request):
    try:
        username = request.data['username']
        email = request.data['email']
        password = request.data['password']
        is_student=request.data['is_student']
        is_instructor=request.data['is_instructor']
        print(request.data)
        #print("entered")
        user = User.objects.get(username=username, email=email, is_student=is_student, is_instructor=is_instructor)
        print(user.username)
        if not user.check_password(password):
            raise ValidationError
        if user:
            try:
                payload = jwt_payload_handler(user)
                print(payload)
                token = jwt.encode(payload, 'SECRET', algorithm='HS256')
                user_details = {}
                user_details['name'] = user.username
                user_details['token'] = token
                user_logged_in.send(sender=user.__class__,
                                    request=request, user=user)
                return Response(user_details, status=status.HTTP_200_OK)

            except Exception as e:
                raise e
        else:
            res = {
                'error': 'can not authenticate with the given credentials or the account has been deactivated'}
            return Response(res, status=status.HTTP_403_FORBIDDEN)
    except:
        res = {'error': 'please provide correct email and a password'}
        return Response(status=status.HTTP_400_BAD_REQUEST)

