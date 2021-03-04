from django.urls import path
from . import views

app_name = "reviews"

urlpatterns = [
    # login reuqired
    path("create/", views.CreateReviewView.as_view(), name="movieReview")
]
