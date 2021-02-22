from django.db import models

# Create your models here
class Movie(models.Model):
    title = models.CharField(max_length=30, null=True, default=True)
    release_date = models.DateField(null=True)
    cast = models.TextField()
    synopsis = models.TextField()
    # change to foreign key
    reviews = models.TextField()
    # change to foreign key
    rating = models.FloatField()