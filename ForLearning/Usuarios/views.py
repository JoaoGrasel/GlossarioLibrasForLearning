from django.shortcuts import render_to_response, render
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login


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
		formulario = UserCreationForm(request.POST)

		if formulario.is_valid():
			user = formulario.save()
			context = { 'user': user }
			return render(request, 'Usuarios/registrar-perfil.html', context)   
		else:
			return render(request, "Usuarios/registrar-usuario.html", {"formulario": formulario})

	return render(request, "Usuarios/registrar-usuario.html", {"formulario": UserCreationForm()})		

def registrar_perfil(request, user):
	if request.method == "POST":
	    formulario = FormularioPerfil(request.POST)
	    if formulario.is_valid():
	        perfil = formulario.save(commit=False)
	        perfil.user = user
	        perfil.save()
	        return redirect('login')
	    else:
	        context = { 'formulario': formulario }
	        return render(request, 'Usuarios/registrar-perfil.html', context)   
	else:
	    formulario = FormularioPerfil()
	    context = { 'formulario': formulario }
	    return render(request, 'Usuarios/registrar-perfil.html', context) 