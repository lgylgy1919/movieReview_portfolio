from django.shortcuts import render
from django.views.generic import ListView, DetailView, View, UpdateView, FormView


class MovieDetailView(DetailView):
    pass


class EditMovieView(UpdateView):
    pass


class CreateMovieView(FormVIiew):
    pass