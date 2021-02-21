from django.contrib.auth.models import AbstractUser
from django.db import models

# User model
class User(AbstractUser):

    """ Custom User Model """

    name = models.CharField(max_length=30, null=True)
    bio = models.TextField(max_length=100, default="Add biography")
    age = models.CharField(max_length=3, null=True)
    email = models.CharField(max_length=100, default="Add your email")
    password = models.CharField(max_length=20, default="Add your password")
    reviews = models.CharField(max_length=100, default="Reviews what you wrote")
