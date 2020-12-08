import json
import jwt
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import viewsets, permissions, status
from rest_framework.decorators import renderer_classes, api_view
from rest_framework.permissions import AllowAny
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from . import serializers
from .models import Course, Deadline, User, Instructor, Student, Ta
from datetime import datetime
from .tasks import send_notifications


class CreateUserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
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
        username = self.request.data['username']
        email = self.request.data['email']
        password = self.request.data['password']
        user = User.objects.create_user(username=username, email=email, password=password)
        user.is_instructor = True
        user.save()
        instructor = Instructor(user=user)
        instructor.save()


class StudentViewSet(viewsets.ModelViewSet):
    def get_queryset(self):
        course = Course.objects.get(code=self.request.GET['code'])
        return course.students.all()

    serializer_class = serializers.StudentSerializer
    permission_classes_by_action = {'create': [AllowAny],
                                    'get_queryset': [permissions.IsAuthenticated]}

    def get_permissions(self):
        try:
            return [permission() for permission in self.permission_classes_by_action[self.action]]
        except KeyError:
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


class TAViewSet(viewsets.ModelViewSet):
    def get_queryset(self):
        course = Course.objects.get(code=self.request.GET['code'])
        return course.tas.all()

    serializer_class = serializers.TaSerializer
    permission_classes_by_action = {
        'create': [AllowAny],
        'get_queryset': [permissions.IsAuthenticated]
    }

    def get_permissions(self):
        try:
            return [permission() for permission in self.permission_classes_by_action[self.action]]
        except KeyError:
            return [permission() for permission in self.permission_classes]

    def perform_create(self, serializer):
        username=self.request.data['username']
        email = self.request.data['email']
        password = self.request.data['password']
        user = User.objects.create_user(username=username, email=email, password=password)
        user.is_ta = True
        user.save()
        ta = Ta(user=user)
        ta.save()


class CourseViewSet(viewsets.ModelViewSet):
    def get_queryset(self):
        return (Course.objects.filter(students__in=[self.request.user.id]) | Course.objects.filter(
            instructor_id=self.request.user.id) | Course.objects.filter(tas__in=[self.request.user.id]))

    serializer_class = serializers.CourseSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def perform_create(self, serializer):
        print(serializer.save(instructor=Instructor.objects.get(user=self.request.user)))

    def perform_update(self, serializer):
        user_instance = serializer.instance
        user_instance.students.add(student_id=self.request.user.id)
        user_instance.save()


class DeadlineViewSet(viewsets.ModelViewSet):
    def get_queryset(self):
        course = Course.objects.get(code=self.request.GET['code'])
        if self.request.user.is_student:
            if not Student.objects.get(user=self.request.user) in course.students.all():
                return Course.objects.none()
        elif self.request.user.is_instructor:
            if self.request.user.id != course.instructor_id:
                return Course.objects.none()
        else:
            if not Ta.objects.get(user=self.request.user) in course.tas.all():
                return Course.objects.none()
        return Deadline.objects.filter(course=course).order_by('-end_date')

    serializer_class = serializers.DeadlineSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def perform_create(self, serializer):
        course = Course.objects.get(code=self.request.GET['code'])
        date = datetime.fromisoformat(self.request.data['end_date'][:-1]).strftime('%Y-%m-%d %H:%M:%S')
        print(date)
        serializer.save(course=course, message=self.request.data['message'], hard=self.request.data['hard'],
                        end_date=date)


@csrf_exempt
@api_view(('POST',))
@renderer_classes((JSONRenderer,))
def updateCourse(request):
    code = json.loads(request.body.decode('utf-8'))['code']
    user = request.user
    course = Course.objects.get(code=code)
    student = Student.objects.get(user_id=user.id)
    course.students.add(student)
    course.save()
    return Response(data=Course.filter(students__in=[user.id]), status=status.HTTP_200_OK)


@csrf_exempt
@api_view(('POST',))
def deleteDeadline(request):
    user = request.user
    id = json.loads(request.body.decode('utf-8'))['id']
    deadline = Deadline.objects.get(id=id)
    try:
        instructor = Instructor.objects.get(user_id=user.id)
        deadline.delete()
        return Response(data=None, status=status.HTTP_200_OK)
    except:
        return Response(data=None, status=status.HTTP_403_FORBIDDEN)


@csrf_exempt
@api_view(('POST',))
@renderer_classes((JSONRenderer,))
def removeStudent(request):
    try:
        instructor = Instructor.objects.get(user=request.user)
        user = User.objects.get(username=json.loads(request.body.decode('utf-8'))['user'])
        student = Student.objects.get(user=user)
        code = json.loads(request.body.decode('utf-8'))['code']
        course = Course.objects.get(code=code)
        course.students.remove(student)
        return Response(data=None, status=status.HTTP_200_OK)
    except:
        return Response(data=None, status=status.HTTP_403_FORBIDDEN)


@csrf_exempt
@api_view(('POST',))
def addTa(request):
    try:
        instructor=Instructor.objects.get(user=request.user)
        user = User.objects.get(username=json.loads(request.body.decode('utf-8'))['username'])
        try:
            ta=Ta.objects.get(user=user)
        except:
            return HttpResponse("TA with given username doesn't exist", status=status.HTTP_400_BAD_REQUEST)
        code = json.loads(request.body.decode('utf-8'))['code']
        course = Course.objects.get(code=code)
        course.tas.add(ta)
        return Response({"username":ta.user.username}, status=status.HTTP_200_OK)
    except:
        return Response({"error":"You are not allowed to perform this action"}, status=status.HTTP_403_FORBIDDEN)

@csrf_exempt
@api_view(('POST',))
def removeTa(request):
    try:
        instructor = Instructor.objects.get(user=request.user)
        user = User.objects.get(username=json.loads(request.body.decode('utf-8'))['user'])
        ta = Ta.objects.get(user=user)
        code = json.loads(request.body.decode('utf-8'))['code']
        course = Course.objects.get(code=code)
        course.tas.remove(ta)
        return Response(data=None, status=status.HTTP_200_OK)
    except:
        return Response(data=None, status=status.HTTP_403_FORBIDDEN)