from django.db import models
from django.urls import reverse
from core import models as core_models


class Movie(core_models.TimeStampedModel):

    """ Movie model Definition """

    title = models.CharField(max_length=30, null=True, default=True)
    genre = models.ManyToManyField("genres.Genre", related_name="movie", blank=True)
    release_date = models.DateField(null=True)
    director = models.CharField(max_length=30, null=True, default=True)
    cast = models.TextField()
    synopsis = models.TextField()

    def total_rating(self):
        all_reviews = self.reviews.all()
        all_rating = 0
        if len(all_reviews) > 0:
            for review in all_reviews:
                all_rating += review.average_rating()
            return round(all_rating / len(all_reviews), 2)
        return 0

    def review(self):
        all_reviews = self.reviews.all()
        return all_reviews

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("movies:movieDetail", kwargs={"pk": self.pk})
