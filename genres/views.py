from django.shortcuts import render
from django.views.generic import FormView
from . import models, forms


class Genre(FormView):
    pass


class CreateGenreView(FormView):
    form_class = forms.CreateGenreForm
    template_name = "genres/genre_create.html"