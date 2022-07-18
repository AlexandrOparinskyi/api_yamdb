from django_filters import filters, FilterSet

from .models import Titles


class TitlesFilters(FilterSet):
    name = filters.CharFilter(
        field_name='name',
        lookup_expr='contains'
    )
    category = filters.CharFilter(
        field_name='category__slug',
        lookup_expr='exact'
    )
    genre = filters.CharFilter(
        field_name='genre__slug',
        lookup_expr='exact'
    )

    class Meta:
        model = Titles
        fields = ('name', 'year', 'category', 'genre')
