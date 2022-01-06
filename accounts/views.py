from django.shortcuts import render
from django.views import generic
from .models import Account
from rest_framework import generics, status, mixins
from .serializers import AccountCreaterSerializer, AccountSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.


class SignUp(mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountCreaterSerializer

    def post(self, request):
        return self.create(request)


class UserDetail(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request, username):
        user = Account.objects.get(username=username)
        serializer = AccountSerializer(user, many=False)
        return Response(serializer.data)

class myProfile(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        user = Account.objects.get(id=request.user.id)
        serializer = AccountSerializer(user, many=False)
        return Response(serializer.data)

