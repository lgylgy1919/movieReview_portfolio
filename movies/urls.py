from django.urls import path
from . import views

app_name = "movies"


urlpatterns = [
    path("/<int:pk>", views.MovieDetailView.as_view(), name="movieDetail"),
    path("/<int:pk>/edit", views.EditMovieView.as_view(), name="movieEdit"),
    path("/create", views.CreateMovieView.as_view(), name="movieCreate"),
]