from django.urls import path
from . import views

app_name = "users"

urlpatterns = [
    path("login/", views.LoginView.as_view(), name="login"),
    path("signup/", views.SignUpView.as_view(), name="signup"),
    # login reuqired
    path("login/<int:pk>/", views.UserDetialView.as_view(), name="userProfile"),
    path("login/<int:pk>/edit/", views.EditProfileView.as_view(), name="editProfile"),
    path("logout/", views.log_out, name="logout"),
]
