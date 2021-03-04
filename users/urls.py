from django.urls import path
from . import views

app_name = "users"

urlpatterns = [
    # login reuqired
    path("<int:pk>/", views.UserDetialView.as_view(), name="userProfile"),
    path("<int:pk>/edit/", views.EditProfileView.as_view(), name="editProfile"),
    path("login/", views.LoginView.as_view(), name="login"),
    path("logout/", views.log_out, name="logout"),
    path("signup/", views.SignUpView.as_view(), name="signup"),
]
