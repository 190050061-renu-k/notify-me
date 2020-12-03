from django.urls import path, include
from rest_framework import routers

from . import views

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'users', views.UserViewSet)
router.register(r'courses', views.CourseViewSet, basename='courses')
router.register(r'deadlines', views.DeadlineViewSet)
#router.register(r'course', views.CourseView.as_view(), basename='course')

urlpatterns = [
#    path(r'api/courses', views.CourseVie),
    path(r'api/', include(router.urls)),
]