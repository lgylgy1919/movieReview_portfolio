from django import forms
from . import models
from genres import models as genre_models
from django.forms.widgets import NumberInput


class SearchForm(forms.Form):
    title = forms.CharField()


class CreateMovieForm(forms.ModelForm):

    genre = forms.ModelMultipleChoiceField(
        queryset=genre_models.Genre.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=True,
    )
    release_date = forms.DateField(widget=NumberInput(attrs={"type": "date"}))

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


class CreatePhotoForm(forms.ModelForm):
    class Meta:
        model = models.Photo
        fields = ("caption", "files")

    def save(self, pk, *args, **kwargs):
        photo = super().save(commit=False)
        movie = models.Movie.objects.get(pk=pk)
        photo.movie = movie
        photo.save()
        return photo
