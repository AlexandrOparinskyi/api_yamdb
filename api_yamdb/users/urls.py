from django.urls import path, include
from rest_framework import routers
from .views import UsersViewSet, user_registration, user_confirmation_code

router = routers.DefaultRouter()
router.register('users', UsersViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('auth/signup/', user_registration),
    path('auth/token/', user_confirmation_code),
]
