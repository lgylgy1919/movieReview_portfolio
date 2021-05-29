from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User
from . import models

"""
admin.site.register(User, UserAdmin)
"""


@admin.register(models.User)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = (
        "username",
        "email",
        "first_name",
        "last_name",
        "manageruser",
    )

    fieldsets = (
        (
            "Individual Information",
            {
                "fields": (
                    "username",
                    "first_name",
                    "last_name",
                    "avatar",
                    "birthday",
                )
            },
        ),
        (
            "Login Information",
            {
                "classes": ("collapse",),
                "fields": ("email", "password"),
            },
        ),
        ("Activity Information", {"fields": ("manageruser",)}),
    )