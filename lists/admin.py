from django.contrib import admin
from .models import List
from . import models


@admin.register(models.List)
class CustomListAdmin(admin.ModelAdmin):
    pass
