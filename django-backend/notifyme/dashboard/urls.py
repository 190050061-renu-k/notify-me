from django.urls import path, include
from rest_framework import routers

from . import views

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'users', views.UserViewSet)
router.register(r'deadlines', views.DeadlineViewSet)

urlpatterns = [
    path(r'api/courses', views.CourseView),
    path(r'api/', include(router.urls)),
]