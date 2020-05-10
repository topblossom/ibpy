from rest_framework import serializers
from icgbooks.shelves.models import Shelf


class ShelfSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shelf
        fields = ('id', 'owner', 'books', 'created_at', 'modified_at')
        read_only_fields = ['created_at', 'modified_at']
