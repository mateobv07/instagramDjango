from django.shortcuts import render
from django.views import generic
from .models import UserProfile, Account
from rest_framework import generics, status, mixins
from .serializers import UserProfileSerializer, AccountCreaterSerializer
# Create your views here.


class SignUp(mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountCreaterSerializer

    def post(self, request):
        return self.create(request)

class UserList(generics.ListCreateAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer

class UserDetail(mixins.RetrieveModelMixin, generics.GenericAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer

    def get(self, request, pk):
        return self.retrieve(request, pk)

