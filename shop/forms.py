from django import forms
from .models import Chocolate


class ChocolateForm(forms.ModelForm):
    class Meta:
        model = Chocolate
        fields = (
            'name', 'price', 'digital', 'image', 'description')
