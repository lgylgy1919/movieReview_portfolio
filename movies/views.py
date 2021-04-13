from django.shortcuts import render, redirect, reverse
from django.views.generic import ListView, DetailView, View, UpdateView, FormView
from . import models, forms
from django.contrib import messages


class HomeView(ListView):
    model = models.Movie
    context_object_name = "movies"


class MovieDetailView(DetailView):
    model = models.Movie
    template_name = "movies/movie_detail.html"


class EditMovieView(UpdateView):
    model = models.Movie
    template_name = "movies/movie_edit.html"
    fields = {
        "title",
        "genre",
        "release_date",
        "director",
        "cast",
        "synopsis",
    }


class CreateMovieView(FormView):

    form_class = forms.CreateMovieForm
    template_name = "movies/movie_create.html"

    """
    def form_valid(self, form):
        movie = form.save()
        movie.host = self.request.user
        movie.save()
        form.save_m2m()
        messages.success(self.request, "Movie Uploaded")
        return redirect(reverse("movies:detail", kwargs={"pk": movie.pk}))
    """


class SearchView(View):
    def get(self, request):
        form = request.GET["searchtitle"]
        return render(request, "search.html", {"form": form})
