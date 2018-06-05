from django import forms
from .models import Perfil

class FormularioPerfil(forms.ModelForm):
    
    class Meta:
        model  = Perfil
        fields = ('nome', 'sobrenome', 'curso', 'universidade')
        
