from rest_framework import serializers
from .models import Employees
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
#from django.contrib.auth import authenticate
from django.contrib.auth import get_user_model

User=get_user_model()



class signupserilaizer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = Employees
        fields = ['empid', 'email', 'password','created_by','updated_by']

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = Employees(**validated_data)
        user.set_password(password)
        user.save()
        return user
    
class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()
    access = serializers.CharField(read_only=True)
    refresh = serializers.CharField(read_only=True)
    def validate(self, data):
        try:
            user = User.objects.get(email=data['email'])
        except User.DoesNotExist:
            raise serializers.ValidationError("Invalid login credentials")

        if not user.check_password(data['password']):
            raise serializers.ValidationError("Invalid login credentials")

        refresh = RefreshToken.for_user(user)
        return {
            'access': str(refresh.access_token),
            'refresh': str(refresh)
        }

class Pageserializer(serializers.ModelSerializer):

    class Meta:
        model = Employees
        fields = ['empid', 'email'] 
        read_only_fields = ['empid', 'email']
    
# class logoutserializer(serializers.Serilaizers):
    