from django.db import models
from core import models as core_models

# Create your models here


class Genre(core_models.TimeStampedModel):

    """ Genre model Definition """

    name = models.CharField(max_length=10, null=True, default=True)
    # link choiced movies to genres : we can know which movies are classified to specific genre
