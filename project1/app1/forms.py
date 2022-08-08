from dataclasses import fields
from django.forms import ModelForm
from . import models

class MoviesForm(ModelForm):
    class Meta:
        model=models.Movies
        fields="__all__"