from django import forms

from .models import Categoria, Sinal

class FormularioSinal(forms.ModelForm):
    
    class Meta:
        model  = Sinal
        fields = ('titulo', 'descricao')