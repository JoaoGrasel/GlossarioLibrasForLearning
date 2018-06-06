from django.shortcuts import render_to_response, render, redirect
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login
from django.contrib.auth.models import User
from .forms import FormularioPerfil

def logar(request):
	if request.method == 'POST':
		formulario = AuthenticationForm(data=request.POST)

		if formulario.is_valid():
			login(request, formulario.get_user())
			return HttpResponseRedirect("/")
		else:
			return render(request, "Usuarios/login.html", {"formulario":formulario})
	return render(request, "Usuarios/login.html", {"formulario": AuthenticationForm()})

def registrar_usuario(request):
	if request.method=='POST':
		formulario_user = UserCreationForm(request.POST)
		formulario_perfil = FormularioPerfil(request.POST)		
		if formulario_user.is_valid() and formulario_perfil.is_valid():
			user = formulario_user.save()
			perfil = formulario_perfil.save(commit=False)	
			perfil.user = user
			perfil.save	
			return redirect('login')   
		else:
			context = {'formulario_user': formulario_user,
                   	   'formulario_perfil': formulario_perfil}
			return render(request, "Usuarios/registrar-usuario.html", context)
	else:
		formulario_user = UserCreationForm()
		formulario_perfil = FormularioPerfil()
		context = {'formulario_user': formulario_user,
                   'formulario_perfil': formulario_perfil}
		return render(request, "Usuarios/registrar-usuario.html", context)		
