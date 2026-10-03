from django import forms
from django.core.validators import RegexValidator

from .models import Order


class CheckoutForm(forms.ModelForm):
    phone = forms.CharField(
        max_length=20,
        validators=[RegexValidator(r"^\+?\d{7,15}$", "Enter a valid phone number.")],
    )

    class Meta:
        model = Order
        fields = ["full_name", "phone", "address"]
        widgets = {"address": forms.Textarea(attrs={"rows": 4})}