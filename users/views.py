from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from rest_framework.viewsets import ModelViewSet

from users.models import CustomUser
from users.serializers import CustomUserSerializer
from users.permissions import IsProfileOwner


class CustomUserViewSet(ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer

    def get_permissions(self):
        if self.action == 'create':
            return [AllowAny(),]
        if self.action in ['update', 'partial_update','retrieve', 'destroy']:
            return [IsAuthenticated(), IsProfileOwner() | IsAdminUser()]
        return [IsAuthenticated()]

