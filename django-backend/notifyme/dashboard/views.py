import json
import jwt
from django.views.decorators.csrf import csrf_exempt
from rest_framework import viewsets, permissions, status
from rest_framework.decorators import renderer_classes, api_view
from rest_framework.permissions import AllowAny
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from . import serializers
from .models import Course, Deadline, User, Instructor, Student


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
        return Response(instructor, status=status.HTTP_201_CREATED)


class StudentViewSet(viewsets.ModelViewSet):
    def get_queryset(self):
        course = Course.objects.get(code=self.request.GET['code'])
        return course.students.all()
    serializer_class = serializers.StudentSerializer
    permission_classes_by_action = {'create': [AllowAny],
                                    'get_queryset': [permissions.IsAuthenticated]}

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
        return (Course.objects.filter(students__in=[self.request.user.id]) | Course.objects.filter(
            instructor_id=self.request.user.id))

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
        return Deadline.objects.filter(course=course).order_by('-end_date')

    serializer_class = serializers.DeadlineSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def perform_create(self, serializer):
        course = Course.objects.get(code=self.request.GET['code'])
        serializer.save(course=course, message=self.request.data['message'], hard=self.request.data['hard'],
                        end_date=self.request.data['end_date'])


@csrf_exempt
@api_view(('POST',))
@renderer_classes((JSONRenderer,))
def updateCourse(request):
    try:
        code = json.loads(request.body.decode('utf-8'))['code']
        token = request.headers['Authorization'][7:]
        user = jwt.decode(token, verify=False)
        course = Course.objects.get(code=code)
        student = Student.objects.get(user_id=user['user_id'])
        course.students.add(student)
        course.save()
        return Response(data=None, status=status.HTTP_200_OK)
    except:
        return Response(data=None, status=status.HTTP_401_UNAUTHORIZED)
