from django.shortcuts import render, redirect, reverse
from django.views.generic import DetailView, UpdateView, FormView
from django.contrib.auth.views import PasswordChangeView
from . import models, forms
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.urls import reverse_lazy
from . import mixins
from reviews.models import Review


class UserProfileView(DetailView):

    model = models.User
    context_object_name = "user_obj"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["reviews"] = Review.objects.all
        return context


class EditProfileView(UpdateView):
    model = models.User
    template_name = "users/profile_edit.html"
    fields = {"first_name", "last_name", "avatar"}


class LoginView(mixins.LoggedOutOnlyView, FormView):
    template_name = "users/login.html"
    form_class = forms.LoginForm
    success_url = reverse_lazy("core:home")

    def form_valid(self, form):
        email = form.cleaned_data.get("email")
        password = form.cleaned_data.get("password")
        user = authenticate(self.request, username=email, password=password)
        if user is not None:
            login(self.request, user)
        return super().form_valid(form)


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
        if user is not None:
            login(self.request, user)
        # user.verify_email()
        return super().form_valid(form)


class ChangePasswordView(PasswordChangeView):
    template_name = "users/update_password.html"

    def get_form(self, form_class=None):
        form = super().get_form(form_class=form_class)
        form.fields["old_password"].widget.attrs = {"placeholder": "Current Password"}
        form.fields["new_password1"].widget.attrs = {"placeholder": "New Password"}
        form.fields["new_password2"].widget.attrs = {
            "placeholder": "Confirm new Password"
        }
        return form

    def get_success_url(self):
        return self.request.user.get_absolute_url()