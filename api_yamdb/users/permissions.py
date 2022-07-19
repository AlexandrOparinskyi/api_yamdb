from rest_framework import permissions


class IsAdminStaffUser(permissions.BasePermission):
    """Автор записи или администратор"""
    def has_permission(self, request, view):
        return (request. user.is_authenticated and
            (request.user.is_admin
            or request.user.is_superuser)
        )


class ModeratorOrReadOnly(permissions.BasePermission):
    """Модератор"""
    def has_permission(self, request, view):
        return (
            request.method in permissions.SAFE_METHODS
            or request.user.is_moderator
        )

    def has_object_permission(self, request, view, obj):
        return obj.author == request.user.is_user


class AuthorOrReadOnly(permissions.BasePermission):
    """Автор"""
    def has_permission(self, request, view):
        return (
            request.method in permissions.SAFE_METHODS
            or request.user.is_authenticated
        )
    # author == поле модели автора, заменить если по другому названо
    def has_object_permission(self, request, view, obj):
        return obj.author == request.user.is_user