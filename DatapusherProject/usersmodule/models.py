from django.db import models
# importing user and manager class
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
#from django.contrib.auth.hashers import make_password, is_password_usable




#Create your models here.
class EmployeeManager(BaseUserManager):
    
        def create_user(self, email, password, **extra_fields):
            if not email:
                raise ValueError("Email must be set")
            if not password:
                raise ValueError("Password must be set")
            email = self.normalize_email(email)
            user = self.model(email=email,password=password,**extra_fields)
            user.save(using=self._db)
            return user  

    
class Employees(AbstractBaseUser, PermissionsMixin):
    empid = models.CharField(max_length=50, primary_key=True)
    email = models.EmailField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey('self', null=True, blank=True, on_delete=models.SET_NULL, related_name='created_emps')
    updated_by = models.ForeignKey('self', null=True, blank=True, on_delete=models.SET_NULL, related_name='updated_emps')
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['empid',]
    objects = EmployeeManager()
    def __str__(self):
        return self.email