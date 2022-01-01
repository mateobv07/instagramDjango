from django.db.models import fields
from rest_framework import serializers
from .models import UserProfile, Account

class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ['id', 'real_name', 'username']

class UserProfileSerializer(serializers.ModelSerializer):
    user = AccountSerializer(read_only=True)
    class Meta:
        model = UserProfile
        fields = '__all__'

class AccountCreaterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = '__all__'