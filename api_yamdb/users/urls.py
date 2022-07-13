from django.urls import path, include
from rest_framework import routers
from users.views import UsersViewSet, RegistrationView, CodeConfirmView


router = routers.DefaultRouter()
router.register('users', UsersViewSet)


urlpatterns = [
    path('', include(router.urls)),
    # path('auth/signup/', RegistrationView.as_view()),
    # path('auth/token/', CodeConfirmView.as_view()),
    
    
]
