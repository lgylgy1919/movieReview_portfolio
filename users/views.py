from django.shortcuts import render, redirect, reverse
from django.views.generic import DetailView, UpdateView, FormView
from . import models, forms
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.urls import reverse_lazy
from . import mixins


class UserDetialView(DetailView):
    model = models.User
    # only login
    template_name = "users/user_profile.html"


class EditProfileView(UpdateView):
    model = models.User
    template_name = "users/profile_edit.html"
    fields = {"first_name", "last_name"}


class LoginView(mixins.LoggedOutOnlyView, FormView):
    template_name = "users/login.html"
    form_class = forms.LoginForm

    def form_valid(self, form):
        email = form.cleaned_data.get("email")
        password = form.cleaned_data.get("password")
        user = authenticate(self.request, username=email, password=password)
        if user is not None:
            login(self.request, user)
        return super().form_valid(form)

    def get_success_url(self):
        next_arg = self.request.GET.get("next")
        if next_arg is not None:
            return next_arg
        else:
            return reverse("core:home")


def log_out(request):
    messages.info(request, f"See you later")
    logout(request)
    return redirect(reverse("core:home"))


class SignUpView(mixins.LoggedOutOnlyView, FormView):
    template_name = "users/signup.html"
    form_class = forms.SignUpForm
    success_url = reverse_lazy("core:home")

    def form_valid(self, form):
        form.save()
        email = form.cleaned_data.get("email")
        password = form.cleaned_data.get("password")
        user = authenticate(self.request, username=email, password=password)
        print(email, password, user)
        if user is not None:
            login(self.request, user)
        # user.verify_email()
        return super().form_valid(form)
