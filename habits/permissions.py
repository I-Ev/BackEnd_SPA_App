from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsAuthor(BasePermission):
    """Права доступа для пользователя"""

    def has_object_permission(self, request, view, obj):
        return request.user == obj.author


class ReadOnly(BasePermission):
    """Права доступа только для чтения """

    def has_permission(self, request, view):
        return request.method in SAFE_METHODS
