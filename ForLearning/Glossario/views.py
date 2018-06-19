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
def index(request):  # ARRUMAR O RETORNO DAS LISTAS DE SINAIS
    if request.user.is_superuser:
        user_logado_id = request.user.id
        perfis = Perfil.objects.all()
        perfil_logado = Perfil.objects.get( user=user_logado_id )
        lista_glossarios = Glossario.objects.filter( pai = None)
        context = {'lista_glossarios': lista_glossarios,
                   'perfil_logado': perfil_logado}

        return render(request, 'Glossario/index.html', context)

    else:
        user_logado_id = request.user.id
        perfis = Perfil.objects.all()
        perfil_logado = Perfil.objects.get( user=user_logado_id )
        lista_glossarios = perfil_logado.glossarios.filter( pai = None)
        lista_glossarios_responsavel = perfil_logado.glossarios_responsavel.filter( pai = None)
        context = {'lista_glossarios': lista_glossarios,
                   'perfil_logado': perfil_logado,
                   'lista_glossarios_responsavel': lista_glossarios_responsavel}

        return render(request, 'Glossario/index.html', context)

@login_required
def conteudo_glossario(request, glossario_id):
    try:
        user_logado_id = request.user.id
        perfis = Perfil.objects.all()
        perfil_logado = Perfil.objects.get( user=user_logado_id )

        glossario = Glossario.objects.get(pk=glossario_id)
        lista_glossarios_filhos = perfil_logado.glossarios.filter(pai = glossario_id)
        lista_glossarios_responsavel = perfil_logado.glossarios_responsavel.filter( pai = glossario_id)

        lista_sinais = Sinal.objects.filter(glossario__id=glossario_id, postado=True)
        
        context = {'lista_sinais': lista_sinais,
                   'glossario': glossario,
                   'perfil_logado': perfil_logado,
                   'lista_glossarios_filhos': lista_glossarios_filhos,
                   'lista_glossarios_responsavel': lista_glossarios_responsavel}
    except Glossario.DoesNotExist:
        raise Http404("Glossario não existe")
    return render(request,'Glossario/sinais-glossario.html', context)

@login_required
def conteudo_tema(request, tema_id):
    try:
        user_logado_id = request.user.id
        perfis = Perfil.objects.all()
        perfil_logado = Perfil.objects.get( user=user_logado_id )
        tema = Tema.objects.get(pk=tema_id)
        lista_sinais = Sinal.objects.filter(tema__id=tema_id, postado=True)
        lista_temas_filhos = Tema.objects.filter(pai = tema_id)
        context = {'lista_sinais': lista_sinais,
                   'tema': tema,
                   'perfil_logado': perfil_logado,
                   'lista_temas_filhos': lista_temas_filhos}
    except Tema.DoesNotExist:
        raise Http404("Tema não existe")
    return render(request,'Glossario/sinais-tema.html', context)

@login_required
def enviar_sinal(request, glossario_id):
    user_logado_id = request.user.id
    perfis = Perfil.objects.all()
    perfil_logado = Perfil.objects.get( user=user_logado_id )
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
                       'perfil_logado': perfil_logado,
                       'formulario': formulario}
            return render(request, 'Glossario/enviar-sinal.html', context)   
    else:
        glossario = Glossario.objects.get(pk=glossario_id)
        formulario = FormularioSinal()
        context = {'glossario': glossario,
                   'perfil_logado': perfil_logado,
                   'formulario': formulario}
        return render(request, 'Glossario/enviar-sinal.html', context) 

@login_required
def conteudo_categorias_glossarios(request):
    try:
        user_logado_id = request.user.id
        perfis = Perfil.objects.all()
        perfil_logado = Perfil.objects.get( user=user_logado_id )

        lista_glossarios = perfil_logado.glossarios.filter( pai = None, postado=True)
        lista_glossarios_filhos_responsavel = perfil_logado.glossarios_responsavel.filter( pai = None)
        context = {'lista_glossarios': lista_glossarios,
                   'perfil_logado': perfil_logado,
                   'lista_glossarios_filhos_responsavel': lista_glossarios_filhos_responsavel}

    except Glossario.DoesNotExist:
        raise Http404("Não existem Glossario")
    return render(request,'Glossario/categorias-glossario.html', context)

@login_required
def conteudo_categorias_temas(request):
    try:
        user_logado_id = request.user.id
        perfis = Perfil.objects.all()
        perfil_logado = Perfil.objects.get( user=user_logado_id )
<<<<<<< HEAD

        lista_tema = Tema.objects.filter( pai = None, postado=True)
        context = {'lista_tema': lista_tema,
                   'perfil_logado': perfil_logado,} 

=======
>>>>>>> a23f358e5d9236e35e0aa28aef30dde921d80df4

        lista_temas = Tema.objects.filter( pai=None, postado=True)
        quantidade_sinais = []

        for tema in lista_temas:
            sinais = Sinal.objects.filter(temas=tema.id, postado=True)
            quantidade_sinais.append(len(sinais))

        context = {'lista_temas': lista_temas,
                   'perfil_logado': perfil_logado,
                   'quantidade_sinais': quantidade_sinais} 


    except Glossario.DoesNotExist:
        raise Http404("Não existem Temas")
    return render(request,'Glossario/categorias-temas.html', context)   


@login_required
def resultado_pesquisa(request):
    return render(request,'Glossario/resultado-pesquisa.html', context)   


# @login_required
# def enviar_glossario(request, glossario_id):
#     user_logado_id = request.user.id
#     perfis = Perfil.objects.all()
#     perfil_logado = Perfil.objects.get( user=user_logado_id )
#     if request.method == "POST":
#         glossario = Glossario.objects.get(pk=glossario_id)
#         formulario = FormularioGlossario(request.POST, request.FILES)
#         if formulario.is_valid():
#             sinal = formulario.save(commit=False)
#             sinal.glossario = glossario
#             sinal.save()
#             return redirect('conteudo-glossario', glossario.id)
#         else:
#             context = {'glossario': glossario,
#                        'perfil_logado': perfil_logado,
#                        'formulario': formulario}
#             return render(request, 'Glossario/enviar-glossario.html', context)   
#     else:
#         glossario = Glossario.objects.get(pk=glossario_id)
#         formulario = FormularioGlossario()
#         context = {'glossario': glossario,
#                    'perfil_logado': perfil_logado,
#                    'formulario': formulario}
#         return render(request, 'Glossario/enviar-glossario.html', context)     