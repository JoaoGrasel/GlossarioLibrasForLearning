from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:glossario_id>/', views.conteudo_glossario, name='conteudo-glossario'),
    path('<int:tema_id>/', views.conteudo_tema, name='conteudo-tema'),
    path('<int:glossario_id>/enviar-sinal/', views.enviar_sinal, name='enviar-sinal')
    path('<int:tema_id>/categorias-temas/', views.categorias_temas, name='categorias-temas')
    path('<int:glossario_id>/categorias-glossario/', views.conteudo_glossario, name='categorias-glossario')
]