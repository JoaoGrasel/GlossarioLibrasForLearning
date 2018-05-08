from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:glossario_id>/', views.conteudo_glossario, name='conteudo-glossario'),
    path('<int:glossario_id>/enviar-sinal/', views.enviar_sinal, name='enviar-sinal')
]