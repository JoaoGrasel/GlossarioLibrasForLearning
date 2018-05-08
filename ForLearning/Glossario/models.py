from django.db import models

# Create your models here.

class Glossario(models.Model):
    titulo = models.CharField(max_length=200)
    
    def __str__(self):
        return self.titulo
        
class Sinal(models.Model):
    glossario = models.ForeignKey(Glossario, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=100)
    descricao = models.TextField()
    arquivo_video = models.FileField(upload_to='videos', null=False)
    postado = models.BooleanField(default=False)
    
    def __str__(self):
        return self.titulo
