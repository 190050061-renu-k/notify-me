from rest_framework import serializers
from .models import Course, Deadline, User, Student, Instructor


class UserSerializer(serializers.HyperlinkedModelSerializer):
    date_joined = serializers.ReadOnlyField()

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password', 'date_joined', 'is_instructor', 'is_student']
        extra_kwargs = {'password': {'write_only': True, 'required': True}}


class StudentSerializer(serializers.ModelSerializer):
    user=serializers.StringRelatedField(many=False)

    class Meta:
        model=Student
        fields=('user')
        fields = '__all__'


class InstructorSerializer(serializers.ModelSerializer):
    user=serializers.StringRelatedField(many=False)

    class Meta:
        model=Instructor
        fields=('user')
        fields = '__all__'


class CourseSerializer(serializers.ModelSerializer):
    students = serializers.StringRelatedField(many=True, required=False, read_only=False)
    instructor = serializers.StringRelatedField(many=False)

    class Meta:
        model = Course
        fields = ('code', 'students', 'instructor', 'date', 'name')
        fields='__all__'


class DeadlineSerializer(serializers.ModelSerializer):
    course=serializers.StringRelatedField(many=False)

    class Meta:
        model = Deadline
        fields = ('id', 'course', 'date', 'message')
