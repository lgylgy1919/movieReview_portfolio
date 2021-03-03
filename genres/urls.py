from django.urls import path
from . import views

app_name = "genres"

urlpatterns = [
    path("", views.Genre.as_view(), name="genre"),
    # login required(only manager )
    path("create/", views.CreateGenreView.as_view(), name="genreCreate"),
]
