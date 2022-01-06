from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import serializers, status
from rest_framework.views import APIView
from .models import Post, Saved
from .serializers import PostSerializer, SavedSerializer, TagSerializer
from rest_framework.permissions import IsAuthenticated

# Create your views here.


class profilePosts(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        posts = Post.objects.filter(user__id=request.user.id)
        serializer = PostSerializer(posts, many=True)
        
        return Response(serializer.data)

class ProfileSaved(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        saved = Saved.objects.filter(user__id=request.user.id)
        serializer = SavedSerializer(saved, many=True)

        return Response(serializer.data)

#Same as above profileSaved, one liner
class ProfileTagged(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        return Response(TagSerializer(request.user.tags.all(), many=True).data)