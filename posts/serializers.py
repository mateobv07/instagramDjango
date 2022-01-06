from django.db import models
from django.db.models import fields
from rest_framework import serializers
from .models import Post, Saved, Tagged
from comments.serializers import CommentSerializer
from accounts.serializers import UsernameSerializer
class PostSerializer(serializers.ModelSerializer):
    comments = serializers.SerializerMethodField()
    tags = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = ('id', 'user', 'description','image','likes','comments', 'tags')

    def get_comments(self, obj):
        return CommentSerializer(obj.comments.all(), many=True).data

    def get_tags(self, obj):
        return TagsOnPost(obj.tags.all(), many=True).data

class SavedSerializer(serializers.ModelSerializer):
    post = PostSerializer(read_only=True)
    class Meta:
        model = Saved
        fields= '__all__'

class TagSerializer(serializers.ModelSerializer):
    post = PostSerializer(read_only=True)
    class Meta:
        model = Tagged
        fields = '__all__'

class TagsOnPost(serializers.ModelSerializer):
    user =  UsernameSerializer(read_only=True)
    class Meta:
        model = Tagged
        fields = ('user',)