from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import CategoriesViewSet, GenresViewSet, TitlesViewSet

router = DefaultRouter()

router.register('categories', CategoriesViewSet)
router.register('genres', GenresViewSet)
router.register('titles', TitlesViewSet)

urlpatterns = [
    path('v1/', include(router.urls))
]
