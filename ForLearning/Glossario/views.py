from django.shortcuts import render, HttpResponse, get_object_or_404, redirect
from django.template import loader
from django.http import Http404, HttpResponseRedirect, HttpResponse
from django.urls import reverse

from .models import Categoria, Sinal
from .forms import FormularioSinal
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
    if request.method == "POST":
        categoria = Categoria.objects.get(pk=categoria_id)
        formulario = FormularioSinal(request.POST)
        if formulario.is_valid():
            sinal = formulario.save(commit=False)
            sinal.categoria = categoria
            sinal.save()
            return redirect('conteudo-categoria', categoria.id)
    else:
        categoria = Categoria.objects.get(pk=categoria_id)
        formulario = FormularioSinal()
        context = {'categoria': categoria,
                   'formulario': formulario}
        return render(request, 'Glossario/enviar-sinal.html', context)    