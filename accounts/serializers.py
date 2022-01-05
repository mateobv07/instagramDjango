from django.db.models import fields
from rest_framework import serializers
from .models import Account, UserFollowing

class AccountSerializer(serializers.ModelSerializer):
    following = serializers.SerializerMethodField()
    followers = serializers.SerializerMethodField()
    class Meta:
        model = Account
        fields = ['id', 'real_name', 'username', 'Description', 'profile_picture', 'following', 'followers']
    
    def get_following(self, obj):
        return FollowingSerializer(obj.following.all(), many=True).data

    def get_followers(self, obj):
        return FollowersSerializer(obj.followers.all(), many=True).data

class AccountCreaterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = '__all__'

class FollowingSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserFollowing
        fields = ("id", "following_user", "created")

class FollowersSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserFollowing
        fields = ("id", "user", "created")