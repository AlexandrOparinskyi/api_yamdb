from django.contrib import admin

from .models import Categories, Genres, Titles


class CategoriesAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'slug')


class GenresAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'slug')


class TitlesAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'year', 'rating',
                    'description', 'category',)


admin.site.register(Categories, CategoriesAdmin)
admin.site.register(Genres, GenresAdmin)
admin.site.register(Titles, TitlesAdmin)
