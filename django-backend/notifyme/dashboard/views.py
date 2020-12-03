from django.contrib.auth.models import User
from rest_framework import viewsets, permissions
from . import serializers
from .models import Course, Deadline


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = serializers.UserSerializer
    permission_classes = ()


class CourseViewSet(viewsets.ModelViewSet):
    def get_queryset(self):
        return Course.objects.filter(user=self.request.user)
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
