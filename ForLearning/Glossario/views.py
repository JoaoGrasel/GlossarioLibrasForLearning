from django.shortcuts import render, HttpResponse, get_object_or_404, redirect
from django.template import loader
from django.http import Http404, HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.db.models import Q
from .models import Glossario, Sinal, Tema
from .forms import FormularioSinal
# Create your views here.

def index(request):
    lista_glossarios = Glossario.objects.filter( pai = None)
    context = {'lista_glossarios': lista_glossarios}
    return render(request, 'Glossario/index.html', context)

def conteudo_glossario(request, glossario_id):
    try:
        glossario = Glossario.objects.get(pk=glossario_id)
        lista_sinais = Sinal.objects.filter(glossario__id=glossario_id, postado=True)
        lista_glossarios_filhos = Glossario.objects.filter(pai = glossario_id)
        context = {'lista_sinais': lista_sinais,
                   'glossario': glossario,
                   'lista_glossarios_filhos': lista_glossarios_filhos}
    except Glossario.DoesNotExist:
        raise Http404("Glossario não existe")
    return render(request,'Glossario/sinais-glossario.html', context)

def conteudo_tema(request, tema_id):
    try:
        tema = Tema.objects.get(pk=tema_id)
        lista_sinais = Sinal.objects.filter(tema__id=glossario_id, postado=True)
        lista_temas_filhos = Tema.objects.filter(pai = tema_id)
        context = {'lista_sinais': lista_sinais,
                   'tema': tema,
                   'lista_temas_filhos': lista_temas_filhos}
    except Tema.DoesNotExist:
        raise Http404("Tema não existe")
    return render(request,'Glossario/sinais-tema.html', context)

def enviar_sinal(request, glossario_id):
    if request.method == "POST":
        glossario = Glossario.objects.get(pk=glossario_id)
        formulario = FormularioSinal(request.POST, request.FILES)
        if formulario.is_valid():
            sinal = formulario.save(commit=False)
            sinal.glossario = glossario
            sinal.save()
            return redirect('conteudo-glossario', glossario.id)
        else:
            context = {'glossario': glossario,
                       'formulario': formulario}
            return render(request, 'Glossario/enviar-sinal.html', context)   
    else:
        glossario = Glossario.objects.get(pk=glossario_id)
        formulario = FormularioSinal()
        context = {'glossario': glossario,
                   'formulario': formulario}
        return render(request, 'Glossario/enviar-sinal.html', context) 


def conteudo_categorias_glossarios(request):
    try:
        lista_glossarios = Glossario.objects.filter( pai = None)
        context = {'lista_glossarios': lista_glossarios}

    except Glossario.DoesNotExist:
        raise Http404("Não existem Glossario")
    return render(request,'Glossario/categorias-glossario.html', context)


def conteudo_categorias_temas(request):
    try:
        lista_tema = Tema.objects.filter( pai = None)
        context = {'lista_tema': lista_tema} 

    except Glossario.DoesNotExist:
        raise Http404("Não existem Temas")
    return render(request,'Glossario/categorias-temas.html', context)    