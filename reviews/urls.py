from django.urls import path
from . import views

app_name = "reviews"

urlpatterns = [
    # login required
    path("create/<int:movie>/", views.CreateReview.as_view(), name="movieReview")
]
