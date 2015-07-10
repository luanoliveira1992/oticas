from django import forms
from Item.models import *
from Item.models import Marca

class MarcaForm(forms.ModelForm):
    success_url = 'success'
    class Meta:
        model = Marca
        exclude = []
        
