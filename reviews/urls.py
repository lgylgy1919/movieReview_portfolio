from django.urls import path
from . import views

app_name = "reviews"

urlpatterns = [
    path("create/<int:movie>/", views.createReviewView.as_view(), name="createReview"),
    path("upload/<int:movie>/", views.upload_review, name="uploadReview"),
    path("detail/<int:review>/", views.ReviewDetailView.as_view(), name="detailReview"),
    path("edit/<int:review>/", views.EditReviewView.as_view(), name="editReview"),
]
