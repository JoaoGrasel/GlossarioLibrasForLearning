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

def registrar(request):
	if request.method=='POST':
		formulario = UserCreationForm(request.POST)

		if formulario.is_valid():
			formulario.save()
			return HttpResponseRedirect("/Usuarios/login/")
		else:
			return render(request, "Usuarios/registrar.html", {"formulario": formulario})

	return render(request, "Usuarios/registrar.html", {"formulario": UserCreationForm()})		