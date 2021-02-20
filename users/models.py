from django.contrib.auth.models import AbstractUser
from django.db import models

# User model
class User(AbstractUser):
    bio = models.CharField(max_length=100, default="Add biography")
