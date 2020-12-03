from django.contrib.auth.models import User
from rest_framework import viewsets, permissions
from . import serializers
from .models import Course, Deadline
from .serializers import CourseSerializer
from django.http.response import JsonResponse, HttpResponse
import jwt


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = serializers.UserSerializer
    permission_classes = ()


class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = serializers.CourseSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class DeadlineViewSet(viewsets.ModelViewSet):
    queryset = Deadline.objects.all()
    serializer_class = serializers.DeadlineSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(course=self.request.course)


def CourseView(request):
    try:
        headers = request.headers
        user = jwt.decode(headers['Authorization'][4:], verify=False)
        courses = Course.objects.filter(user=User.objects.all()[user['user_id'] - 1])
        course_serializer = CourseSerializer(courses, many=True)
        return JsonResponse(course_serializer.data, safe=False)
    except:
        return HttpResponse("Please Login Again")
