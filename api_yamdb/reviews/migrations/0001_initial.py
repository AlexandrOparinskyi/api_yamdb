# Generated by Django 2.2.16 on 2022-07-18 11:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256, verbose_name='Название категории')),
                ('slug', models.CharField(max_length=50, unique=True, verbose_name='Slug категории')),
            ],
        ),
        migrations.CreateModel(
            name='Genres',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256, verbose_name='Название жанра')),
                ('slug', models.CharField(max_length=50, unique=True, verbose_name='Slug жанра')),
            ],
        ),
        migrations.CreateModel(
            name='Titles',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Название произведения')),
                ('year', models.IntegerField(verbose_name='Год выпуска')),
                ('rating', models.IntegerField(blank=True, default=None, null=True)),
                ('description', models.TextField(blank=True, null=True, verbose_name='Описание произведения')),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='categories', to='reviews.Categories')),
                ('genre', models.ManyToManyField(to='reviews.Genres')),
            ],
        ),
    ]
