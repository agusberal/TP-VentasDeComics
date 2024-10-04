#-->importamos Forms
from django import forms
#-->importamos los modelos/tablas
from .models import *

class NuevoComics(forms.ModelForm):
    class Meta:
        model=Comics
        fields='__all__'