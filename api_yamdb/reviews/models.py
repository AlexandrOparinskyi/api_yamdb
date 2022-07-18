from django.db import models


class Categories(models.Model):
    name = models.CharField(
        'Название категории',
        max_length=256,
    )
    slug = models.CharField(
        'Slug категории',
        max_length=50,
        unique=True,
    )

    def __str__(self):
        return self.name


class Genres(models.Model):
    name = models.CharField(
        'Название жанра',
        max_length=256,
    )
    slug = models.CharField(
        'Slug жанра',
        max_length=50,
        unique=True,
    )

    def __str__(self):
        return self.name


class Titles(models.Model):
    name = models.CharField(
        'Название произведения',
        max_length=50,
    )
    year = models.IntegerField(
        'Год выпуска',
    )
    rating = models.IntegerField(
        default=None,
        null=True,
        blank=True,
    )
    description = models.TextField(
        'Описание произведения',
        null=True,
        blank=True,
    )
    genre = models.ManyToManyField(
        Genres,
        through='GenresTitles'
    )
    category = models.ForeignKey(
        Categories,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='categories',
    )

    def __str__(self):
        return self.name


class GenresTitles(models.Model):
    genre = models.ForeignKey(Genres, on_delete=models.CASCADE)
    titles = models.ForeignKey(Titles, on_delete=models.CASCADE)
