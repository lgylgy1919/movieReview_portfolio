from django.contrib import messages
from django.shortcuts import render, redirect, reverse
from django.views.generic import FormView, View, UpdateView
from movies import models as movie_models
from . import models, forms
from reviews import forms as review_form

# 해당 영화의 pk를 가져와야 한다. 어떻게???


class createReviewView(View):
    def get(self, *args, **kwargs):
        pk = kwargs["movie"]
        movie = movie_models.Movie.objects.get(pk=pk)
        form = review_form.CreateReviewForm()
        return render(
            self.request,
            "mixins/review/review_form.html",
            {"form": form, "movie": movie, "pk": pk},
        )


def upload_review(request, movie):
    if request.method == "POST":
        form = forms.CreateReviewForm(request.POST)
        movie = movie_models.Movie.objects.get(pk=movie)

        if form.is_valid():
            review = form.save()
            review.movie = movie
            review.writer = request.user
            review.save()
            messages.success(request, "Movie Reviewed")
            return redirect(reverse("movies:movieDetail", kwargs={"pk": movie.pk}))

    return redirect(reverse("core:home"))


class EditReviewView(UpdateView):
    model = models.Review
    template_name = "reviews/review_edit.html"
    fields = {"story", "ost", "visual", "director", "acting", "comment"}
