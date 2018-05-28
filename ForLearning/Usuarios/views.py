from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.views.generic.base import View
from Glossario.models import Perfil
from Usuarios.forms import RegistrarUsuarioForm

class RegistrarUsuarioView(View):
	
	template_name = 'registrar.html'

	def get(self, request, *args, **kwargs):
		return render(request, self.template_name)
		
	def post(self, request, *args, **kwargs):

		form = RegistrarUsuarioForm(request.POST)

		if form.is_valid():

			dados_form = form.data

			usuario = User.objects.create_user(dados_form['nome'], 
				dados_form['email'], dados_form['senha'])

			perfil = Perfil(nome=dados_form['nome'], 
							email=dados_form['email'], 
							curso=dados_form['curso'],
							universidade=dados_form['universidade'],
							usuario=usuario)

			perfil.save()

			return redirect('index')

		return render(request, self.template_name, {'form' : form})