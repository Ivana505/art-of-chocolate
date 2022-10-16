from django import forms
from .models import Chocolate, Category


class ChocolateForm(forms.ModelForm):
    class Meta:
        model = Chocolate
        fields = (
            'name', 'price', 'category', 'digital', 'image', 'description')
