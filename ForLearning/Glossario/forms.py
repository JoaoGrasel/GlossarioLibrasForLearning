from django import forms
from .models import Glossario,  Tema , Sinal

class FormularioSinal(forms.ModelForm):
    
    class Meta:
        model  = Sinal
        fields = ('titulo', 'descricao', 'sinal_video', 'conceito_video')


class FormularioGlossario(forms.ModelForm):

    class Meta:
        model  = Glossario
        fields = ('titulo', 'pai' )

   
class FormularioTema(forms.ModelForm):

    class Meta:
        model  = Tema
        fields = ('titulo',)