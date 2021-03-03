from django.shortcuts import render
from django.views.generic import DetailView, UpdateView, FormView
from . import models


class UserDetialView(DetailView):
    model = models.User
    # unknown
    template_name = "users/user_profile.html"


class EditProfileView(UpdateView):
    model = models.User
    template_name = "users/profile_edit.html"
    fields = {"first_name", "last_name"}


class LoginView(FormView):
    pass


class LogOutView(FormView):
    pass


class SignUpView(FormView):
    pass