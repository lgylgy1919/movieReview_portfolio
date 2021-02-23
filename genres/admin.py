from django.contrib import admin
from . import models


@admin.register(models.Genre)
class GenreAdmin(admin.ModelAdmin):

    # add count_movies
    list_display = ("name",)
