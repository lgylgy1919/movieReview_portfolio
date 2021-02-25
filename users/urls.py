from django.urls import path
from . import views

app_name = "users"

urlpatterns = [
    path("<int:pk>", views.UserDetialView.as_view(), name="userProfile"),
    path("<int:pk>/edit", views.EditProfileView.as_view(), name="editProfile"),
]
