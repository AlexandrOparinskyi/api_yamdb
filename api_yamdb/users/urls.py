from django.urls import include, path
from rest_framework import routers

from .views import UsersViewSet, user_confirmation_code, user_registration

router = routers.DefaultRouter()
router.register('users', UsersViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('auth/signup/', user_registration),
    path('auth/token/', user_confirmation_code),
]
