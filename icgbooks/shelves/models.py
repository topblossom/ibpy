from django.db import models
from icgbooks.books.models import Book
from icgbooks.users.models import User
class Shelf(models.Model):
    title = models.TextField()
    owner = models.ForeignKey(User)
    books = models.ManyToManyField(Book)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

