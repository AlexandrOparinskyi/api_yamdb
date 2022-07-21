from rest_framework import filters, viewsets, mixins
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticatedOrReadOnly


from django.shortcuts import get_object_or_404
from reviews.models import Categories, Genres, Titles, Review
from reviews.filters import TitlesFilters
from users.permissions import IsAdminOrReadOnly, ModeratorOrReadOnly
from .serializers import (CategoriesSerializer,
                          GenresSerializer,
                          TitlesSerializer,
                          TitlePostSerializer,
                          CommentSerializer,
                          ReviewSerializer)


class CategoriesViewSet(mixins.ListModelMixin,
                        mixins.CreateModelMixin,
                        mixins.DestroyModelMixin,
                        viewsets.GenericViewSet):
    queryset = Categories.objects.all()
    serializer_class = CategoriesSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name',)
    permission_classes = [IsAdminOrReadOnly]

    def get_object(self):
        return Categories.objects.get(slug=self.kwargs['pk'])


class GenresViewSet(CategoriesViewSet):
    queryset = Genres.objects.all()
    serializer_class = GenresSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name',)
    permission_classes = [IsAdminOrReadOnly]

    def get_object(self, queryset=None):
        return Genres.objects.get(slug=self.kwargs['pk'])


class TitlesViewSet(viewsets.ModelViewSet):
    queryset = Titles.objects.all()
    http_method_names = ['post', 'get', 'patch', 'delete']
    filter_backends = (DjangoFilterBackend,)
    filterset_class = TitlesFilters
    permission_classes = [IsAdminOrReadOnly]

    def get_serializer_class(self):
        if self.action in ('create', 'update', 'partial_update'):
            return TitlePostSerializer
        return TitlesSerializer


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = (
        IsAuthenticatedOrReadOnly, ModeratorOrReadOnly
    )

    def get_queryset(self):
        review = get_object_or_404(Review, id=self.kwargs.get('review_id'))
        return review.comments.all()

    def perform_create(self, serializer):
        review = get_object_or_404(Review, id=self.kwargs.get('review_id'))
        serializer.save(author=self.request.user, review=review)


class ReviewViewSet(viewsets.ModelViewSet):
    serializer_class = ReviewSerializer
    permission_classes = (
        IsAuthenticatedOrReadOnly, ModeratorOrReadOnly, IsAdminOrReadOnly
    )

    def get_queryset(self):
        title = get_object_or_404(Titles, id=self.kwargs.get('title_id'))
        return title.reviews.all()

    def perform_create(self, serializer):
        title = get_object_or_404(Titles, id=self.kwargs.get('title_id'))
        serializer.save(author=self.request.user, title=title)
