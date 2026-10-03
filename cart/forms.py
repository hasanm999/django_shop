from django import forms

# Safety limit only (prevents absurd values / integer overflow), not a stock limit.
MAX_QUANTITY = 99999999999


class QuantityForm(forms.Form):
    quantity = forms.IntegerField(min_value=1, max_value=MAX_QUANTITY, initial=1)