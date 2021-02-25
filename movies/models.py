from django.db import models
from core import models as core_models

# Create your models here
class Movie(core_models.TimeStampedModel):

    """ Movie model Definition """

    title = models.CharField(max_length=30, null=True, default=True)
    genre = models.ManyToManyField("genres.Genre", related_name="movie", blank=True)
    release_date = models.DateField(null=True)
    director = models.CharField(max_length=30, null=True, default=True)
    cast = models.TextField()
    synopsis = models.TextField()
    # change to foreign key
    reviews = models.ManyToManyField(
        "reviews.Review", related_name="movies", blank=True
    )

    def total_rating(self):
        all_rating = 5
        return all_rating

    def __str__(self):
        return self.title