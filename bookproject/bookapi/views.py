from django.shortcuts import render
from rest_framework import viewsets
from .models import Book
from .serializers import BookSerializer , UserSerializer
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

