from django.contrib import messages
from django.shortcuts import render, redirect, reverse
from django.views.generic import FormView
from movies import models as movie_models
from . import models, forms


class CreateReviewView(FormView):
    form_class = forms.CreateReviewForm
    template_name = "reviews/review_create.html"


"""
def enroll_review(request, movie):
    if request.method == "POST":
        movie = movie_models.Movie.objects.get_or_none(pk=movie)
        if not movie:
            return redirect(reverse("core:home"))
        if form.is_valid():
            review = form.save()
            review.movie = movie
            review.writer = request.user
            review.save()
            messages.success(request, "New Movie reviewed")
            return redirect(reverse("movie:detail", kwargs={"pk": movie.pk}))
"""
