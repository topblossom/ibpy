from rest_framework import viewsets
from .models import Shelf
from .serializers import ShelfSerializer

class ShelfViewSet(viewsets.ModelViewSet):
    def get_queryset(self):
        user = self.request.user
        return Shelf.objects.filter(owner=user)

    queryset = Shelf.objects.all().order_by('created_at')
    serializer_class = ShelfSerializer
