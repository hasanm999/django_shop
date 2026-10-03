from django import forms
from .models import Rating


class RatingForm(forms.ModelForm):
    score = forms.TypedChoiceField(
        label="Your rating",
        choices=[(i, f"{i} star{'s' if i > 1 else ''}") for i in range(1, 6)],
        coerce=int,
        widget=forms.RadioSelect,
    )

    class Meta:
        model = Rating
        fields = ["score"]