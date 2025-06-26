from django.db import models
import uuid
import secrets
from django.db import models
from django.contrib.auth import get_user_model  # get the customised model(authmodel) which is in settings.py not default user model

User = get_user_model()

class Account(models.Model):
    account_id = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    account_name = models.CharField(max_length=255)
    app_secret_token = models.CharField(max_length=64,editable=False,unique=True)
    website = models.URLField(max_length=500,blank=True,null=True)
    created_at = models.DateTimeField(auto_now_add=True,editable=False)
    updated_at = models.DateTimeField(auto_now=True,editable=False)
    created_by = models.ForeignKey(User,related_name='accounts_created',on_delete=models.CASCADE,editable=False)
    updated_by = models.ForeignKey(User,related_name='accounts_updated',on_delete=models.CASCADE,editable=False,null=True)
    
    def save(self, *args, **kwargs):
        # Generate a token only once on creation
        if not self.app_secret_token:
            self.app_secret_token = secrets.token_hex(32)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.account_name
