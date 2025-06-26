from django.urls import path
from .views import RegisterUserView,LoginView,PageView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('registeruser/',RegisterUserView.as_view()),
    path('loginuser/',LoginView.as_view()),
    path('Page1/',PageView.as_view()),
    
    
    path('logintoken/', TokenObtainPairView.as_view()),
    path('token/refresh/', TokenRefreshView.as_view())
]
