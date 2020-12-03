from django.urls import include, path
from rest_framework import routers
from dashboard import views
from django.contrib import admin
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('admin/',admin.site.urls),
    path('', include(router.urls)),
    path('dashboard', include('dashboard.urls')),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path(r'api-token-auth/', obtain_jwt_token),
    path(r'api-token-refresh/', refresh_jwt_token),
]