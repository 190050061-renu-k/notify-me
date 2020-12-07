from django.urls import path, include
from rest_framework import routers

from . import views

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'users', views.CreateUserViewSet)
router.register(r'courses', views.CourseViewSet, basename='courses')
router.register(r'deadlines', views.DeadlineViewSet, basename='deadlines')
router.register(r'instructors', views.InstructorViewSet)
router.register(r'students', views.StudentViewSet, basename='students')

urlpatterns = [
    path(r'api/', include(router.urls)),
    path(r'api/addStudenttoCourse', views.updateCourse),
    path(r'api/deleteDeadline', views.deleteDeadline),
    path(r'api/removeStudent', views.removeStudent),
]