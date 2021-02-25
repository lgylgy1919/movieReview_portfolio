from django.shortcuts import render
from django.views.generic import ListView, FormView, UpdateView
from movies.models import Movie


class HomeView(ListView):
    model = Movie
