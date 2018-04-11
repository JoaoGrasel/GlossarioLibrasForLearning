from django.shortcuts import render, HttpResponse
from django.template import loader
from django.http import Http404

from .models import Categoria
# Create your views here.

def index(request):
    lista_ultimas_categorias = Categoria.objects.order_by('-pub_date')[:5]
    context = {'lista_ultimas_categorias': lista_ultimas_categorias}
    return render(request, 'Glossario/index.trabalho.html', context)

def conteudo_categoria(request, categoria_id):
    try:
        categoria = Categoria.objects.get(pk=categoria_id)
    except Categoria.DoesNotExist:
        raise Http404("Categoria não existe")
    return render(request,'Glossario/index.trabalho.html', {'categoria':categoria})

def enviar_sinal(request, categoria_id):
    return HttpResponse("Enviar Sinal para categoria %s" % categoria_id)

def sinal_enviado_sucesso(request):
    return HttpResponse("Sinal enviado com sucesso")