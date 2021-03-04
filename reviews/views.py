from django.shortcuts import render
from django.views.generic import FormView
from . import models, forms


class CreateReviewView(FormView):
    form_class = forms.CreateReviewForm
    template_name = "reviews/review_create.html"