from rest_framework import serializers
from .models import Comment
class CommentSerializer(serializers.ModelSerializer):
    username = serializers.SerializerMethodField('comment_user')
    def comment_user(self, thisuser):
        return thisuser.user.username
    class Meta:
        model = Comment
        fields = ('id', 'post', 'comment','created_at','username')