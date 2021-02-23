from django.db import models
from core import models as core_models


class Review(core_models.TimeStampedModel):

    story = models.IntegerField()
    ost = models.IntegerField()
    visual = models.IntegerField()
    director = models.IntegerField()
    acting = models.IntegerField()
    review = models.TextField()

    movie = models.ForeignKey("movies.Movie", on_delete=models.CASCADE)
    writer = models.ForeignKey("users.User", on_delete=models.CASCADE)