# from django.db import models
# from django.contrib.auth.models import User

# class Perfil(models.Model):

# 	nome = models.CharField(max_length=200, null=False)
# 	universidade = models.CharField(max_length=200, null=False)
# 	curso = models.CharField(max_length=200, null=False)
# 	usuario = models.OneToOneField(User, related_name="Usuario")

# 	@property
# 	def email(self):
# 		return self.usuario.email

# 		