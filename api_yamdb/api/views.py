from rest_framework import filters, viewsets, mixins
from django_filters.rest_framework import DjangoFilterBackend

from reviews.models import Categories, Genres, Titles
from reviews.filters import TitlesFilters
from .serializers import (CategoriesSerializer,
                          GenresSerializer,
                          TitlesSerializer,
                          TitlePostSerializer)


class CategoriesViewSet(mixins.ListModelMixin,
                        mixins.CreateModelMixin,
                        mixins.DestroyModelMixin,
                        viewsets.GenericViewSet):
    queryset = Categories.objects.all()
    serializer_class = CategoriesSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name',)

    def get_object(self):
        return Categories.objects.get(slug=self.kwargs['pk'])


class GenresViewSet(CategoriesViewSet):
    queryset = Genres.objects.all()
    serializer_class = GenresSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name',)

    def get_object(self, queryset=None):
        return Genres.objects.get(slug=self.kwargs['pk'])


class TitlesViewSet(viewsets.ModelViewSet):
    queryset = Titles.objects.all()
    http_method_names = ['post', 'get', 'patch', 'delete']
    filter_backends = (DjangoFilterBackend,)
    filterset_class = TitlesFilters

    def get_serializer_class(self):
        if self.action in ('create', 'update', 'partial_update'):
            return TitlePostSerializer
        return TitlesSerializer
