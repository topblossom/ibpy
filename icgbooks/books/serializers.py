from rest_framework import serializers
from icgbooks.books import models


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Book
        fields = ('id', 'title', 'pages', 'created_at', 'modified_at')
        read_only_fields = ['created_at', 'modified_at']
