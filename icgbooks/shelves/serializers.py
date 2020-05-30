from rest_framework import serializers
from icgbooks.shelves.models import Shelf


class ShelfSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shelf
        fields = ('id', 'owner', 'books', 'title', 'created_at', 'modified_at')
        read_only_fields = ('id','created_at', 'modified_at', 'owner')
