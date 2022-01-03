from django.shortcuts import render
from django.views import generic
from .models import UserProfile, Account
from rest_framework import generics, status, mixins
from .serializers import UserProfileSerializer, AccountCreaterSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.


class SignUp(mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountCreaterSerializer

    def post(self, request):
        return self.create(request)

class UserList(generics.ListCreateAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer

class UserDetail(APIView):
    def get(self, request, username):
        user = UserProfile.objects.get(user__username=username)
        serializer = UserProfileSerializer(user, many=False)
        return Response(serializer.data)

class myProfile(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        user = UserProfile.objects.get(user=request.user)
        serializer = UserProfileSerializer(user, many=False)
        return Response(serializer.data)

