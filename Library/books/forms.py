from django import forms
from django.forms import ModelForm
from .models import Notes


class BookForm(forms.ModelForm):
    class Meta:
        model = Notes
        fields = ('title', 'semester', 'Branch', 'pdf', )