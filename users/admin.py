from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User
from . import models

"""
admin.site.register(User, UserAdmin)
"""


@admin.register(models.User)
class CustomUserAdmin(admin.ModelAdmin):
    pass