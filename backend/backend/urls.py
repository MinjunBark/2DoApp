from django.contrib import admin
from django.urls import path, include
# api/views
from api.views import CreateUserView
# JWT Token 
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/user/register/', CreateUserView.as_view(), name='register'), # linked our registration view
    path('api/token/', TokenObtainPairView.as_view(), name='get_token'), # linked token obtain pair view
    path('api/token/refresh', TokenRefreshView.as_view(), name='refresh'), # linked token refresh view
    path('api-auth/', include("rest_framework.urls")), # linked all pre-built urls we need from rest framework
    path('api/', include('api.urls')),
]
