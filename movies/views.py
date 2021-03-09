from django.shortcuts import render
from django.views.generic import ListView, DetailView, View, UpdateView, FormView
from . import models, forms


class HomeView(ListView):
    model = models.Movie
    context_object_name = "movies"


class MovieDetailView(DetailView):
    model = models.Movie
    template_name = "movies/movie_detail.html"


class EditMovieView(UpdateView):
    model = models.Movie
    template_name = "movies/movie_edit.html"


class CreateMovieView(FormView):

    form_class = forms.CreateMovieForm
    template_name = "movies/movie_create.html"


class SearchView(View):
    def get(self, request):
        form = request.GET["searchtitle"]
        return render(request, "search.html", {"form": form})
