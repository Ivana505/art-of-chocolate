from django import forms
from .models import Contact


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = (
            'name', 'email_address', 'phone', 'message'
        )
        fields_required = ['name', 'email_address', 'phone', 'message']

