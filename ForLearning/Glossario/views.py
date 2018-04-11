from django.shortcuts import render, HttpResponse
from django.template import loader
from django.http import Http404

from .models import Categoria, Sinal
# Create your views here.

def index(request):
    lista_categorias = Categoria.objects.all()
    context = {'lista_categorias': lista_categorias}
    return render(request, 'Glossario/index.trabalho.html', context)

def conteudo_categoria(request, categoria_id):
    try:
        categoria = Categoria.objects.get(pk=categoria_id)
        lista_sinais = Sinal.objects.all()
        context = {'lista_sinais': lista_sinais}
    except Categoria.DoesNotExist:
        raise Http404("Categoria não existe")
    return render(request,'Glossario/video1.html', {'categoria':categoria}, context)

def enviar_sinal(request, categoria_id):
    return HttpResponse("Enviar Sinal para categoria %s" % categoria_id)

def sinal_enviado_sucesso(request):
    return HttpResponse("Sinal enviado com sucesso")