from django.shortcuts import render, HttpResponse, get_object_or_404, redirect
from django.http import Http404, HttpResponseRedirect, HttpResponse, request
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Glossario, Sinal, Tema, Perfil
from django.template import loader
from django.urls import reverse
from django.db.models import Q
from .forms import FormularioSinal
# Create your views here.

@login_required
def index(request):
    user_logado_id = request.user.id
    perfis = Perfil.objects.all()
    perfil_logado = Perfil.objects.get( user=user_logado_id )
    lista_glossarios = perfil_logado.glossarios.filter( pai = None)
    context = {'lista_glossarios': lista_glossarios}
    return render(request, 'Glossario/index.html', context)

#alem de só mostrar o conteudo do glossario em questao, tambem só pode mostrar o conteudo que o usuario tem acesso
@login_required
def conteudo_glossario(request, glossario_id):
    try:
        user_logado_id = request.user.id
        perfis = Perfil.objects.all()
        perfil_logado = Perfil.objects.get( user=user_logado_id )

        glossario = Glossario.objects.get(pk=glossario_id)
        lista_glossarios_filhos = perfil_logado.glossarios.filter(pai = glossario_id)

        lista_sinais = Sinal.objects.filter(glossario__id=glossario_id, postado=True)
        
        context = {'lista_sinais': lista_sinais,
                   'glossario': glossario,
                   'lista_glossarios_filhos': lista_glossarios_filhos}
    except Glossario.DoesNotExist:
        raise Http404("Glossario não existe")
    return render(request,'Glossario/sinais-glossario.html', context)

#alem de só mostrar o conteudo do tema em questao, tambem só pode mostrar o conteudo que o usuario tem acesso
@login_required
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

@login_required
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

@login_required
def conteudo_categorias_glossarios(request):
    try:
        user_logado_id = request.user.id
        perfis = Perfil.objects.all()
        perfil_logado = Perfil.objects.get( user=user_logado_id )
        
        lista_glossarios = perfil_logado.glossarios.filter( pai = None, postado=True)
        context = {'lista_glossarios': lista_glossarios}

    except Glossario.DoesNotExist:
        raise Http404("Não existem Glossario")
    return render(request,'Glossario/categorias-glossario.html', context)

@login_required
def conteudo_categorias_temas(request):
    try:
        lista_tema = Tema.objects.filter( pai = None, postado=True)
        context = {'lista_tema': lista_tema} 

    except Glossario.DoesNotExist:
        raise Http404("Não existem Temas")
    return render(request,'Glossario/categorias-temas.html', context)   

    