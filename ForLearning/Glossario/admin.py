from django.contrib import admin

from .models import Glossario, Sinal, Tema, Perfil

# Register your models here.

admin.site.register(Glossario)
admin.site.register(Sinal)
admin.site.register(Tema)
admin.site.register(Perfil)