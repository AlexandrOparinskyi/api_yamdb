from rest_framework import permissions


class IsAdminStaffUser(permissions.BasePermission):
    """Автор записи или администратор"""
    def has_permission(self, request, view):
        return (request.user.is_authenticated and
                    (request.user.is_admin
                        or request.user.is_superuser)
                )


class IsAdminOrReadOnly(permissions.BasePermission):
    """Только администратор"""
    def has_permission(self, request, view):
        return (request.method in permissions.SAFE_METHODS or (
                    request.user.is_authenticated and (
                        request.user.role == 'admin'
                        or request.user.is_superuser
                        )
                    )
                )
