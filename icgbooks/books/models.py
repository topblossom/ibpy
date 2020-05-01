from django.db import models


class Book(models.Model):
    title = models.TextField()
    pages = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    # class Meta:
    #     app_label = 'icgbooks.books'
