from django.db import models
# from Perfis.models import Perfil

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
        
class Sinal(models.Model):
    glossario = models.ForeignKey(Glossario, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=100)
    descricao = models.TextField()
    arquivo_video = models.FileField(upload_to='videos', null=False)
    postado = models.BooleanField(default=False)
    temas = models.ManyToManyField(Tema)
    # responsavel = models.ForeignKey(Perfil, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.titulo

