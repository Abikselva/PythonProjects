from rest_framework import serializers
from .models import Account

class AccountSerializer(serializers.ModelSerializer):
    created_by = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = Account
        fields = ['account_name','website']