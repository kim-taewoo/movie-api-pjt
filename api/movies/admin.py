from django.contrib import admin
from .models import Movie, Genre, Actor, Director

class MovieAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'title',
        'sub_title',
        'poster',
        'rating',
        'pub_date',
        'runtime',
        'audits',
        'audi_cnt',
    ]

admin.site.register(Movie, MovieAdmin)
admin.site.register(Genre)
admin.site.register(Actor)
admin.site.register(Director)