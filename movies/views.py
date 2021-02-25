from django.shortcuts import render
from django.views.generic import ListView, DetailView, View, UpdateView, FormView


class MovieDetailView(DetailView):
    pass


class EditMovieView(UpdateView):
    pass


class CreateMovieView(FormView):

    template_name = "movies/movie_create.html"