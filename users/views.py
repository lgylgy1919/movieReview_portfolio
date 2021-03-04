from django.shortcuts import render, redirect, reverse
from django.views.generic import DetailView, UpdateView, FormView
from . import models, forms
from django.contrib import messages
from django.contrib.auth import login, logout


class UserDetialView(DetailView):
    model = models.User
    # unknown
    template_name = "users/user_profile.html"


class EditProfileView(UpdateView):
    model = models.User
    template_name = "users/profile_edit.html"
    fields = {"first_name", "last_name"}


class LoginView(FormView):
    template_name = "users/login.html"
    form_class = forms.LoginFrom


def log_out(request):
    messages.info(request, f"See you later")
    logout(request)
    return redirect(reverse("core:home"))


class SignUpView(FormView):
    template_name = "users/signup.html"
    form_class = forms.SignUpForm