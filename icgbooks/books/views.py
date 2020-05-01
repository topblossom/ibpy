from rest_framework import viewsets
from icgbooks.books.models import Book
from icgbooks.books.serializers import BookSerializer


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
