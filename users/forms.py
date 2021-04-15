from django import forms
from . import models


class LoginForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(attrs={"placeholder": "Email"}))
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={"placeholder": "Password"})
    )


class SignUpForm(forms.ModelForm):
    class Meta:
        model = models.User
        fields = (
            "username",
            "first_name",
            "last_name",
            "bio",
            "birthday",
        )

        widgets = {
            "username": forms.TextInput(attrs={"palceholder": "username"}),
            "first_name": forms.TextInput(attrs={"placeholder": "First Name"}),
            "last_name": forms.TextInput(attrs={"placeholder": "Last Name"}),
            "email": forms.EmailInput(attrs={"placeholder": "Email"}),
            "bio": forms.TextInput(attrs={"placeholder": "bio"}),
        }

    password = forms.CharField(
        widget=forms.PasswordInput(attrs={"placeholder": "Password"})
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={"placeholder": "confirm Password"})
    )
