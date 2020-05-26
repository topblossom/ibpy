from rest_framework import viewsets, mixins
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated
from rest_framework.response import Response
from rest_framework.request import Request
from .models import User
from .serializers import CreateUserSerializer, UserSerializer, UserProfileSerializer
from rest_framework.schemas.openapi import AutoSchema

class UserViewSet(mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin,
                  viewsets.GenericViewSet):
    """
    Updates and retrieves user accounts
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAdminUser,)


class UserCreateViewSet(mixins.CreateModelMixin,
                        viewsets.GenericViewSet):
    """
    Creates user accounts
    """
    queryset = User.objects.all()
    serializer_class = CreateUserSerializer
    permission_classes = (AllowAny,)

class UserProfileView(APIView):
    permission_classes = [IsAuthenticated]
    schema = AutoSchema()

    def get(self, request: Request, format=None) -> Response:
        """
        Handles user profile.
        """
        self.schema = AutoSchema()
        return Response(UserProfileSerializer(request.user).data)
