from django.contrib.auth.models import AbstractUser
from django.db import models

# User model
class User(AbstractUser):

    """ Custom User Model """

    username = models.CharField(max_length=30, unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    bio = models.TextField(max_length=100, default="Add biography")
    birthday = models.DateField(null=True)
    avatar = models.ImageField(null=True, blank=True)

    email = models.EmailField(max_length=256)
    password = models.CharField(max_length=256)
    # change to foreign Key,
    reviews = models.ManyToManyField("reviews.Review", related_name="user", blank=True)
    manageruser = models.BooleanField(default=False)

    def count_reviews(self):
        all_reviews = 5
        return all_reviews