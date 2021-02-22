from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User
from . import models

"""
admin.site.register(User, UserAdmin)
"""


@admin.register(models.User)
class CustomUserAdmin(admin.ModelAdmin):
    fieldsets = (
        (
            "Individual Information",
            {"fields": ("username", "avatar", "birthday", "bio")},
        ),
        (
            "Login Information",
            {
                "classes": ("collapse",),
                "fields": ("email", "password"),
            },
        ),
        ("Activity Information", {"fields": ("reviews",)}),
    )