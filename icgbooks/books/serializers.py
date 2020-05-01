from rest_framework import serializers
from icgbooks.books import models


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Book
        fields = ('id', 'title', 'pages')
        read_only_fields = ['created_at', 'updated_at', 'modified_at']
