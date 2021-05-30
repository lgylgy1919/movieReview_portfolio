from django import forms
from . import models


class SearchForm(forms.Form):
    title = forms.CharField()


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

    def save(self, *args, **kwargs):
        movie = super().save(commit=False)
        return movie
