from django.shortcuts import render

# Create your views here.

from django.contrib.auth.models import User
from rest_framework.generics import (ListCreateAPIView,RetrieveUpdateDestroyAPIView)
from app2.serializers import UserSerializer
from app2.models import User
from rest_framework import permissions
from app2.permissions import IsOwnerOrReadOnly
from rest_framework import generics


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

