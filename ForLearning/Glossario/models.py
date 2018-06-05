from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

# Create your models here.

class Glossario(models.Model):
    titulo = models.CharField(max_length=200)
    pai = models.ForeignKey("self", on_delete=models.CASCADE, default=None, blank=True, null=True)
    postado = models.BooleanField(default=False)

    def __str__(self):
        return self.titulo

class Tema(models.Model):

    titulo = models.CharField(max_length=200)
    pai = models.ForeignKey("self", on_delete=models.CASCADE, default=None, blank=True, null=True)
    postado = models.BooleanField(default=False)
    
    def __str__(self):
        return self.titulo;


class Perfil(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    nome = models.CharField(max_length=255, null=False) 
    sobrenome = models.CharField(max_length=255, null=True) 
    curso = models.CharField(max_length=255, null=True) 
    universidade = models.CharField(max_length=255, null=True) 
    responsavel = models.BooleanField(default=False)


    def __str__(self):
        return this.nome

def cria_user_Perfil(sender, instance, created, **kwargs):
    if created:
        Perfil.objects.create(user=instance)

post_save.connect(cria_user_Perfil, sender=User)

class Sinal(models.Model):
    glossario = models.ForeignKey(Glossario, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=100)
    descricao = models.TextField()
    arquivo_video = models.FileField(upload_to='videos', null=False)
    postado = models.BooleanField(default=False)
    temas = models.ManyToManyField(Tema)
    responsavel = models.ForeignKey(Perfil, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.titulo

