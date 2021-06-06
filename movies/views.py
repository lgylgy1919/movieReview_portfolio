from django.shortcuts import render, redirect, reverse
from django.views.generic import ListView, DetailView, View, UpdateView, FormView
from . import models, forms
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from users import mixins as user_mixins
from reviews import forms as review_form


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

    def form_valid(self, form):
        movie = form.save()
        movie.host = self.request.user
        movie.save()
        form.save_m2m()
        messages.success(self.request, "Movie Uploaded")
        return redirect(reverse("movies:movieDetail", kwargs={"pk": movie.pk}))


class MoviePhotosView(DetailView):
    model = models.Movie
    template_name = "movies/movie_photos.html"

    def get_object(self, queryset=None):
        movie = super().get_object(queryset=queryset)
        return movie


class AddPhotoView(user_mixins.LoggedInOnlyView, FormView):

    model = models.Photo
    template_name = "movies/photo_create.html"
    form_class = forms.CreatePhotoForm
    fields = (
        "caption",
        "files",
    )

    def form_valid(self, form):
        pk = self.kwargs.get("pk")
        form.save(pk)
        messages.success(self.request, "Photo Uploaded")
        return redirect(reverse("movies:photos", kwargs={"pk": pk}))


def delete_photo(request, movie_pk, photo_pk):

    models.Photo.objects.filter(pk=photo_pk).delete()
    messages.success(request, "Photo Deleted")
    return redirect(reverse("movies:photos", kwargs={"pk": movie_pk}))


class EditPhotoView(SuccessMessageMixin, UpdateView):
    model = models.Photo
    template_name = "movies/photo_edit.html"
    pk_url_kwarg = "photo_pk"
    success_message = "Photo Updated"
    fields = ("caption",)

    def get_success_url(self):
        movie_pk = self.kwargs.get("movie_pk")
        return reverse("movies:photos", kwargs={"pk": movie_pk})


class SearchView(View):
    def get(self, request):
        title = request.GET["searchtitle"]
        # qs = models.Movie.objects.filter(**{"title": title}).order_by("-created")
        qs = models.Movie.objects.filter(title__icontains=title)
        return render(request, "search.html", {"movies": qs})
