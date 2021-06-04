from django.urls import path
from . import views

app_name = "movies"


urlpatterns = [
    path("<int:pk>/", views.MovieDetailView.as_view(), name="movieDetail"),
    # login reuqired( only manager )
    path("<int:pk>/edit/", views.EditMovieView.as_view(), name="movieEdit"),
    path("create/", views.CreateMovieView.as_view(), name="movieCreate"),
    path("search/", views.SearchView.as_view(), name="search"),
    path("<int:pk>/photos/", views.MoviePhotosView.as_view(), name="photos"),
    path("<int:pk>/photos/add", views.AddPhotoView.as_view(), name="add-photo"),
    path(
        "<int:movie_pk>/photos/<int:photo_pk>/delete/",
        views.delete_photo,
        name="delete-photo",
    ),
    path(
        "<int:movie_pk>/photos/<int:photo_pk>/edit/",
        views.EditPhotoView.as_view(),
        name="edit-photo",
    ),
]