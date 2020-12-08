import jwt
from django.contrib.auth import user_logged_in
from rest_framework import status, exceptions
from rest_framework.decorators import api_view, permission_classes
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework_jwt.serializers import jwt_payload_handler
from dashboard.models import User, Student
import datetime


@api_view(['POST'])
@permission_classes([AllowAny, ])
def authenticate_user(request):
    try:
        username = request.data['username']
        password = request.data['password']
        email=request.data['email']
        is_student = request.data['is_student']
        is_instructor = request.data['is_instructor']
        user = User.objects.get(username=username, email=email, is_student=is_student, is_instructor=is_instructor)
        if is_student:
            student = Student.objects.get(user=user)
            student.registration_token = request.data['registration_token']
            student.save()
        if not user.check_password(password):
            raise ValidationError
        try:
            payload = jwt_payload_handler(user)
            token = jwt.encode(payload, 'SECRET', algorithm='HS256')
            response = Response()
            refresh_token_payload = {
                'user_id': user.id,
                'exp': datetime.datetime.utcnow() + datetime.timedelta(days=7),
                'iat': datetime.datetime.utcnow()
            }
            refresh_token = jwt.encode(refresh_token_payload, 'REFRESH_TOKEN_SECRET').decode('utf-8')
            response.set_cookie(key='refresh_token', value=refresh_token, httponly=True)
            response.data = {
                'token': token,
                'user': user.username,
            }
            user_logged_in.send(sender=user.__class__,
                                request=request, user=user)
            return response

        except Exception as e:
            raise e
    except:
        res = {'error': 'Please provide correct credentials'}
        return Response(res, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def refresh_token_view(request):
    try:
        refresh_token = request.COOKIES.get('refresh_token')
        try:
            payload = jwt.decode(refresh_token, 'REFRESH_TOKEN_SECRET', algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            return Response("Session expired, please login again", status=status.HTTP_401_UNAUTHORIZED)
        user = User.objects.get(id=payload.get('user_id'))
        access_token = jwt.encode(jwt_payload_handler(user), 'SECRET', algorithm='HS256')
        return Response({'token': access_token})
    except:
        return Response("Wrong Credentials, please login again", status=status.HTTP_403_FORBIDDEN)

@api_view(['POST'])
def logout(request):
        student=Student.objects.get(user=request.user)
        student.registration_token=""
        student.save()
        return Response("Successful logout", status=status.HTTP_200_OK)