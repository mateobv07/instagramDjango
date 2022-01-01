from django.shortcuts import render
from django.views import generic
from .models import UserProfile
from rest_framework import generics, status, mixins
from .serializers import UserProfileSerializer
# Create your views here.

class UserList(generics.ListCreateAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer

class UserDetail(mixins.RetrieveModelMixin, generics.GenericAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer

    def get(self, request, pk):
        return self.retrieve(request, pk)