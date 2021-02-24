from django.db import models
from core import models as core_models

# Create your models here
class Movie(core_models.TimeStampedModel):

    """ Movie model Definition """

    title = models.CharField(max_length=30, null=True, default=True)
    genre = models.ManyToManyField("genres.Genre", related_name="genre")
    release_date = models.DateField(null=True)
    director = models.CharField(max_length=30, null=True, default=True)
    cast = models.TextField()
    synopsis = models.TextField()
    # change to foreign key
    reviews = models.TextField()
    # change to foreign key
    rating = models.FloatField()

    def __str__(self):
        return self.title