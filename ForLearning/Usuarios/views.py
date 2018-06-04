from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.views.generic.base import View
from Glossario.models import Perfil
from Usuarios.forms import RegistrarUsuarioForm, FormularioLogin
from django.contrib.auth import authenticate, login


def login_view(request):

	if request.method == "POST":
		formulario = FormularioLogin(request.POST)
		if formulario.is_valid():
			dados_form = formulario.data
			username = dados_form['username']
			senha = dados_form['senha']
			user = authenticate(username=username, password=senha)
			if user is not None:
				return redirect(request, 'index')
			else:
				return render(request, 'Usuarios/login.html')

		else:
			formulario = FormularioLogin()
			return render(request, 'Usuarios/login.html')

def registrar_usuario_view(request):
	if request.method == "POST":		
		formulario = RegistrarUsuarioForm(request.POST)
		if formulario.is_valid():
			dados_form = formulario.data
			usuario = User.objects.create_user(dados_form['username'], 
							 				   dados_form['email'], 
							 				   dados_form['senha'])
			perfil = Perfil(nome=dados_form['nome'], 
							usuario=usuario)
			perfil.save()
			return redirect('index')	
		else: 
			return render(request, 'Usuarios/registrar.html') 
	else: 
		formulario = RegistrarUsuarioForm()
		return render(request, 'Usuarios/registrar.html') 
