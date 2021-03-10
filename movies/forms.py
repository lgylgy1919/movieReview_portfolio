from django import forms
from . import models


class CreateMovieForm(forms.ModelForm):
    class Meta:
        model = models.Movie
        fields = (
            "title",
            "genre",
            "release_date",
            "director",
            "cast",
            "synopsis",
        )
