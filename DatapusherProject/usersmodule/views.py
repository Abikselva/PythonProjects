from django.shortcuts import render
from rest_framework import generics
from rest_framework.decorators import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import AllowAny,IsAuthenticated
#from .models import Employees
from .serializers import signupserilaizer,LoginSerializer,Pageserializer
from rest_framework.response import Response
from rest_framework import status
# sign up for user class


class RegisterUserView(generics.CreateAPIView):
    serializer_class = signupserilaizer
    permission_classes = [AllowAny]
    
class LoginView(generics.GenericAPIView):
    serializer_class = LoginSerializer
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        return Response({
            'message': 'Login successful',
            'access': serializer.validated_data['access'],
            'refresh': serializer.validated_data['refresh']
        }, status=status.HTTP_200_OK)

class PageView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        serializer = Pageserializer(request.user)
        return Response({
            "message": "You are authenticated!",
            **serializer.data
        })
        
        

    
    