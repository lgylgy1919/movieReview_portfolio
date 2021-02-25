from django.urls import path
from . import views

app_name = "lists"

urlpatterns = [path("", views.List.as_view(), name="lists")]
