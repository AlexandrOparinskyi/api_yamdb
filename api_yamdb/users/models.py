from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    class Role:
        ADMIN = 'admin'
        USER = 'user'
        MODERATOR = 'moderator'
        USER_ROLE = (
            (ADMIN, 'Admin'),
            (USER, 'User'),
            (MODERATOR, 'Moderator'),
        )
    bio = models.TextField(
        verbose_name='User bio',
        blank=True,
        null=True,
    )
    email = models.EmailField(
        verbose_name='User email',
        unique=True,
    )
    role = models.CharField(
        verbose_name='User role',
        max_length=15,
        choices=Role.USER_ROLE,
        default=Role.USER
    )

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    @property
    def is_moderator(self):
        return (
            self.role == self.Role.MODERATOR
        )

    @property
    def is_admin(self):
        return (
            self.role == self.Role.ADMIN
            or self.is_superuser
        )

    @property
    def is_user(self):
        return (
            self.role == self.Role.USER
        )
