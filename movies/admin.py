from django.contrib import admin
from .models import Movie
from . import models

# Register your models here.
@admin.register(models.Movie)
class CustomMovieAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "release_date",
        "rating",
    )
