from django import forms
from .models import *


class Insertform(forms.ModelForm):
    class Meta:
        model = Music
        fields = ['song', 'album', 'title']
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Enter Title', 'class': 'form-control mb-2'}),
        }
