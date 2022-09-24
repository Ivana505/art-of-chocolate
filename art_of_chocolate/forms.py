from .models import Chocolate
from django import forms


class ChocolateForm(forms.ModelForm):
    class Meta:
        model = Chocolatefields = (
            'name', 'price'
        )