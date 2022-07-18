from rest_framework import serializers

from reviews.models import Categories, Genres, Titles, GenresTitles


class CategoriesSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('name', 'slug',)
        model = Categories


class GenresSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('name', 'slug',)
        model = Genres


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

    class Meta:
        fields = ('id', 'name', 'year', 'rating',
                  'description', 'genre', 'category',)
        model = Titles

    def to_representation(self, instance):
        serializer = TitlesSerializer(instance)
        return serializer.data

    def create(self, validated_data):
        genres = validated_data.pop('genre')
        title = Titles.objects.create(**validated_data)
        for genre in genres:
            current_genre, _ = Genres.objects.get_or_create(
                name=genre
            )
            GenresTitles.objects.create(
                genre=current_genre, titles=title
            )
        return title

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.year = validated_data.get('year', instance.year)
        instance.rating = validated_data.get('rating', instance.rating)
        instance.description = validated_data.get(
            'description',
            instance.description
        )
        instance.genre = validated_data.get('genre', instance.genre)
        instance.category = validated_data.get('category', instance.category)
        instance.save()
        return instance