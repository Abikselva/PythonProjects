from django.urls import path
from .views import AccountCreateAPIView
urlpatterns = [
    path('createaccount/',AccountCreateAPIView.as_view()),
]