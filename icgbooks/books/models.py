from django.db import models


class Book(models.Model):
    title = models.TextField()
    pages = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.title}, {self.pages} pages'

    # class Meta:
    #     app_label = 'icgbooks.books'
