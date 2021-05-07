from django import forms
from . import models


class CreateReviewForm(forms.ModelForm):

    story = forms.IntegerField(max_value=5, min_value=1)
    ost = forms.IntegerField(max_value=5, min_value=1)
    visual = forms.IntegerField(max_value=5, min_value=1)
    director = forms.IntegerField(max_value=5, min_value=1)
    acting = forms.IntegerField(max_value=5, min_value=1)

    class Meta:
        model = models.Review
        fields = (
            "story",
            "ost",
            "visual",
            "director",
            "acting",
            "comment",
            "movie",
            "writer",
        )