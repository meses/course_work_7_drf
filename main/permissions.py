from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    """Пользователь может работать только со своими привычками."""

    def has_object_permission(self, request, view, obj):
        # Разрешить чтение любому пользователю
        if request.method in permissions.SAFE_METHODS:
            return True

        # Разрешить запись только владельцу привычки
        return obj.user == request.user


class IsPublicOrReadOnly(permissions.BasePermission):
    """Пользователь может видеть список публичных привычек без возможности их как-то редактировать или удалять."""

    def has_object_permission(self, request, view, obj):

        # Разрешить запись только владельцу привычки
        if obj.public is True:
            return True
        elif obj.public is False and obj.user != request.user:
            return False
        else:
            return False
