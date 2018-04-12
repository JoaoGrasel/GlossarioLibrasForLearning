from django.shortcuts import render, HttpResponse, get_object_or_404
from django.template import loader
from django.http import Http404, HttpResponseRedirect, HttpResponse
from django.urls import reverse

from .models import Categoria, Sinal
# Create your views here.

def index(request):
    lista_categorias = Categoria.objects.all()
    context = {'lista_categorias': lista_categorias}
    return render(request, 'Glossario/index.html', context)

def conteudo_categoria(request, categoria_id):
    try:
        categoria = Categoria.objects.get(pk=categoria_id)
        lista_sinais = Sinal.objects.all()
        context = {'lista_sinais': lista_sinais,
                   'categoria': categoria}
    except Categoria.DoesNotExist:
        raise Http404("Categoria não existe")
    return render(request,'Glossario/sinais.html', context)

def enviar_sinal(request, categoria_id):
    categoria = Categoria.objects.get(pk=categoria_id)
    context = {'categoria': categoria}
    return render(request, 'Glossario/enviar-sinal.html', context)

def sinal_enviado_sucesso(request, categoria_id):
    categoria = Categoria.objects.get(pk=categoria_id)
    sinal = Sinal()
    try:
        titulo_escrito = sinal.titulo_set.get(pk=request.POST['titulo'])
        descricao_escrita = sinal.descricao_set.get(pk=request.POST['descricao'])
        categoria_selecionada = sinal.categoria_set(categoria)
    except (KeyError, Sinal.DoesNotExist):
        return render(request, 'Glossario/enviar-categoria.html', {
            'categoria': categoria,
            'mensagem_erro': "Você deixou um campo em branco",
        })
    
    else:
        sinal.save()
        return HttpResponseRedirect(reverse('Glossario/index.html', args=(sinal.id)))
        