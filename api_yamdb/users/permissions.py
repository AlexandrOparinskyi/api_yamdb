from rest_framework import permissions


class IsAdminStaffUser(permissions.BasePermission):
    """Автор записи или администратор"""
    def has_permission(self, request, view):
        return (request.user.is_authenticated and
                    (request.user.is_admin
                        or request.user.is_superuser)
                )


class IsAdminOrReadOnly(permissions.BasePermission):
    """Разрешает доступ только для администратора или только для чтения"""
    def has_permission(self, request, view):
        return (request.method in permissions.SAFE_METHODS or (
                    request.user.is_authenticated and (
                        request.user.role == 'admin'
                        or request.user.is_superuser
                        )
                    )
                )


class ModeratorOrReadOnly(permissions.BasePermission):
    """Модератор"""
    def has_permission(self, request, view):
        return (
            request.method in permissions.SAFE_METHODS
            or request.user.is_moderator
        )

    def has_object_permission(self, request, view, obj):
        return request.user.is_moderator


class AuthorOrReadOnly(permissions.BasePermission):
    """Автор"""
    def has_permission(self, request, view):
        return (
            request.method in permissions.SAFE_METHODS
            or request.user.is_authenticated
        )
    # author == поле модели автора, заменить если по другому названо

class AuthorModeratorOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        return (
            request.method in permissions.SAFE_METHODS
            or request.user.is_authenticated
        )

    def has_object_permission(self, request, view, obj):
        return (
            request.method in permissions.SAFE_METHODS
            or obj.author == request.user
            or request.user.is_moderator
            or request.user.is_admin
        )