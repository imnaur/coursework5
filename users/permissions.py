from rest_framework import permissions
from rest_framework.permissions import BasePermission


class IsUserOrReadOnlyIfPublic(BasePermission):
    """Разрешает чтение, если привычка публичная. Редактирование и удаление — только для создателя."""

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS and obj.public:
            return True
        return obj.user == request.user

class IsProfileOwner(BasePermission):
    """Отдельный permission для юзера (доступ к своим данным)"""
    def has_permission(self, request, view, obj):
        return obj == request.user