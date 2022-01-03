from rest_framework import serializers
from .models import Post
from comments.serializers import CommentSerializer
from comments.models import Comment
from accounts.serializers import AccountSerializer

class PostSerializer(serializers.ModelSerializer):
    user = AccountSerializer(read_only=True)
    comments = serializers.SerializerMethodField('comment_count')
    def comment_count(self, thispost):
        com = Comment.objects.filter(post=thispost)
        com_serializer = CommentSerializer(com, many=True)
        return com_serializer.data
    class Meta:
        model = Post
        fields = ('id', 'user', 'description','image','likes','comments')