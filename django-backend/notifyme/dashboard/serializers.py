from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Course, Deadline


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True, 'required': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user


class CourseSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(many=False)

    class Meta:
        model = Course
        fields = ('id', 'user', 'date', 'name')


class DeadlineSerializer(serializers.ModelSerializer):
    course=serializers.StringRelatedField(many=False)

    class Meta:
        model = Deadline
        fields = ('id', 'course', 'date', 'message')
