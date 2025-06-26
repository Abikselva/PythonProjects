from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import AllowAny,IsAuthenticated
from .serializers import AccountSerializer
# Create your views here.
class AccountCreateAPIView(generics.CreateAPIView):
    serializer_class = AccountSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)