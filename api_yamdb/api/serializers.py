import datetime
from rest_framework import serializers

from reviews.models import Categories, Genres, Titles, Review, Comment
from django.core.validators import MaxValueValidator, MinValueValidator
from django.shortcuts import get_object_or_404
from rest_framework.permissions import SAFE_METHODS


class CategoriesSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('name', 'slug',)
        model = Categories


class GenresSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('name', 'slug',)
        model = Genres


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True, slug_field='username',
        default=serializers.CurrentUserDefault(),
    )

    class Meta:
        model = Comment
        fields = ('id', 'text', 'author', 'pub_date', 'review')
        read_only_fields = ('review',)


class ReviewSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True, slug_field='username',
        default=serializers.CurrentUserDefault(),
    )
    title = serializers.SlugRelatedField(
        read_only=True, slug_field='name',
    )
    score = serializers.IntegerField(
        validators=[MaxValueValidator(10), MinValueValidator(1)]
    )

    def validate(self, data):
        if (self.context['request'].method in SAFE_METHODS
           or self.context['request'].method == 'PATCH'):
            return data
        title_id = self.context['view'].kwargs.get('title_id')
        title = get_object_or_404(Titles, id=title_id)
        reviews = self.context['request'].user.reviews
        if reviews.filter(title=title).exists():
            raise serializers.ValidationError(
                'Вы уже оставляли отзыв на это произведение!'
            )
        return data

    class Meta:
        model = Review
        fields = ('id', 'title', 'text', 'author', 'score', 'pub_date')


class TitlesSerializer(serializers.ModelSerializer):
    category = CategoriesSerializer(
        read_only=True
    )
    genre = GenresSerializer(
        read_only=True,
        many=True,
    )

    class Meta:
        fields = ('id', 'name', 'year', 'rating',
                  'description', 'genre', 'category',)
        model = Titles


class TitlePostSerializer(serializers.ModelSerializer):
    category = serializers.SlugRelatedField(
        slug_field='slug',
        queryset=Categories.objects.all(),
    )
    genre = serializers.SlugRelatedField(
        slug_field='slug',
        queryset=Genres.objects.all(),
        many=True
    )
    year = serializers.IntegerField(
        validators=[MaxValueValidator(datetime.datetime.now().year)]
    )

    class Meta:
        fields = ('id', 'name', 'year', 'rating',
                  'description', 'genre', 'category',)
        model = Titles

    def to_representation(self, instance):
        serializer = TitlesSerializer(instance)
        return serializer.data

    def create(self, validated_data):
        category = validated_data.pop('category')
        genres = validated_data.pop('genre')
        title = Titles.objects.create(category=category, **validated_data)
        for genre in genres:
            title.genre.add(genre)
        return title

