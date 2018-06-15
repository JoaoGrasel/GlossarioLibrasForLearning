from django import forms
from .models import Glossario, Sinal, Tema

class FormularioSinal(forms.ModelForm):
    
    class Meta:
        model  = Sinal
        fields = ('titulo', 'descricao', 'arquivo_video')
<<<<<<< HEAD
      

# class FormularioGlossario(forms.ModelForm):
    
#     class Meta:
#         model  = Glossario
#         fields = ('titulo')
=======
        
>>>>>>> 45d3efd2287f5289261abc39eaa3fe7f232ca9d6
