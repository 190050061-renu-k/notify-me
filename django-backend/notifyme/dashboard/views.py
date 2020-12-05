import jwt
from django.contrib.auth import user_logged_in
from django.shortcuts import redirect
from rest_framework import viewsets, permissions, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework_jwt.serializers import jwt_payload_handler

from . import serializers
from .models import Course, Deadline, User, Instructor, Student



class CreateUserViewSet(viewsets.ModelViewSet):
    # Allow any user (authenticated or not) to access this url
    queryset=User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = serializers.UserSerializer

    def perform_create(self, serializer):
        user = self.request.data
        serializer = serializers.UserSerializer(data=user)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class InstructorViewSet(viewsets.ModelViewSet):
    queryset = Instructor.objects.all()
    serializer_class = serializers.InstructorSerializer
    permission_classes = (AllowAny,)

    def perform_create(self, serializer):
        print(self.request.data)
        username=self.request.data['username']
        email=self.request.data['email']
        password=self.request.data['password']
        user = User.objects.create_user(username=username, email=email, password=password)
        user.is_instructor=True
        user.save()
        instructor = Instructor(user=user)
        instructor.save()
        return Response(instructor, status=status.HTTP_201_CREATED)


class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = serializers.StudentSerializer
    permission_classes_by_action = {'create':[AllowAny],
                          'get_queryset':[permissions.IsAuthenticated]}

    def get_permissions(self):
        try:
            # return permission_classes depending on `action`
            return [permission() for permission in self.permission_classes_by_action[self.action]]
        except KeyError:
            # action is not set return default permission_classes
            return [permission() for permission in self.permission_classes]

    def perform_create(self, serializer):
        username = self.request.data['username']
        email = self.request.data['email']
        password = self.request.data['password']
        user = User.objects.create_user(username=username, email=email, password=password)
        user.is_student = True
        user.save()
        student = Student(user=user)
        student.save()
        return Response(student, status=status.HTTP_201_CREATED)


class CourseViewSet(viewsets.ModelViewSet):
    def get_queryset(self):
        return ( Course.objects.filter(students__in=[self.request.user.id])|Course.objects.filter(instructor_id=self.request.user.id))
    serializer_class = serializers.CourseSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def perform_create(self, serializer):
        print(serializer)
        ins=Instructor.get(user=self.request.user)

        serializer.save(instructor=ins)


class DeadlineViewSet(viewsets.ModelViewSet):
    queryset = Deadline.objects.all()
    serializer_class = serializers.DeadlineSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(course=self.request.course)