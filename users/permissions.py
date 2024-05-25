from rest_framework import permissions


class IsCreator(permissions.BasePermission):
    """
    Вводит ограничения по создателю привычки
    """
    def has_object_permission(self, request, view, obj):
        return obj.creator == request.user
