from django.db import models
from django.contrib.auth.models import User

class Perfil(models.Model):

	nome = models.CharField(max_length=255, null=False) 
	telefone = models.CharField(max_length=15, null=False)
	nome_empresa = models.CharField(max_length=255, null=False)
	contatos = models.ManyToManyField('self')
	usuario = models.OneToOneField(User, related_name="perfil", on_delete=models.CASCADE)

	def __str__(self):
		return this.nome

	@property
	def email(self):
		return self.usuario.email

