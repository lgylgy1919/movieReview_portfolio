from django.contrib import messages
from django.shortcuts import render, redirect, reverse
from django.views.generic import FormView
from movies import models as movie_models
from . import models, forms


class CreateReview(FormView):
    template_name = "reviews/review_create.html"
    form_class = forms.CreateReviewForm

    def get_success_url(self):

        return reverse("core:home")
