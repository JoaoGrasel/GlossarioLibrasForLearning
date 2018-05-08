from django import forms
from .models import Glossario, Sinal

class FormularioSinal(forms.ModelForm):
    
    class Meta:
        model  = Sinal
        fields = ('titulo', 'descricao', 'arquivo_video')
        
