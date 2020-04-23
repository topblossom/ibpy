from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import permissions
from .models import Book
from .serializers import BookSerializer


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

