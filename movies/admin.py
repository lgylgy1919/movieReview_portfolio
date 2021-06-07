from django.contrib import admin
from .models import Movie
from django.utils.html import mark_safe

from . import models

# Register your models here.
@admin.register(models.Movie)
class CustomMovieAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "release_date",
        "total_rating",
    )


@admin.register(models.Photo)
class PhotoAdmin(admin.ModelAdmin):

    """ Photo admin Definition """

    list_display = ("__str__", "get_thumbnail")

    def get_thumbnail(self, obj):
        return mark_safe(f"<img width=50px scr='{obj.files.url}' />")

    get_thumbnail.short_description = "Thumbnail"
