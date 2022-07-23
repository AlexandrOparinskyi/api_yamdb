from django.urls import include, path
from rest_framework import routers

from .views import UsersViewSet, user_confirmation_code, user_registration

router = routers.DefaultRouter()
router.register('users', UsersViewSet)


urlpatterns = [
    path('v1/', include(router.urls)),
    path('v1/auth/signup/', user_registration),
    path('v1/auth/token/', user_confirmation_code),
]
