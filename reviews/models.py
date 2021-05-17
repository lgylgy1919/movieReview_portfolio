from django.db import models
from core import models as core_models


class Review(core_models.TimeStampedModel):

    story = models.IntegerField()
    ost = models.IntegerField()
    visual = models.IntegerField()
    director = models.IntegerField()
    acting = models.IntegerField()
    comment = models.TextField()

    movie = models.ForeignKey(
        "movies.Movie", related_name="reviews", on_delete=models.CASCADE
    )
    writer = models.ForeignKey("users.User", on_delete=models.CASCADE, null=True)

    def average_rating(self):
        average_rating = (
            self.story + self.ost + self.visual + self.director + self.acting
        ) / 5
        return round(average_rating, 2)

    average_rating.short_description = "AVG."
