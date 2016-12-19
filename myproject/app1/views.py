from django.shortcuts import render
from rest_framework import status
from rest_framework import generics
from app1.models import Snippet
from app1.serializers import SnippetSerializer

class SnippetList(generics.ListCreateAPIView):
    queryset=Snippet.objects.all()
    serializer_class=SnippetSerializer

class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset=Snippet.objects.all()
    serializer_class=SnippetSerializer
