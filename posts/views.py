from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import serializers, status
from rest_framework.views import APIView
from .models import Post
from .serializers import PostSerializer
from rest_framework.permissions import IsAuthenticated

# Create your views here.


class profilePosts(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        posts = Post.objects.filter(user__id=request.user.id)
        serializer = PostSerializer(posts, many=True)
        
        return Response(serializer.data)

