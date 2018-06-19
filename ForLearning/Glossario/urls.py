from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('conteudo-categorias-glossarios/<int:glossario_id>/', views.conteudo_glossario, name='conteudo-glossario'),
    path('conteudo-categorias-temas/<int:tema_id>/', views.conteudo_tema, name='conteudo-tema'),
    path('<int:glossario_id>/enviar-sinal/', views.enviar_sinal, name='enviar-sinal'),
    path('conteudo-categorias-temas/', views.conteudo_categorias_temas, name='conteudo-categorias-temas'),
    path('conteudo-categorias-glossarios/', views.conteudo_categorias_glossarios, name='conteudo-categorias-glossarios'),
<<<<<<< HEAD
    path('resultado-pesquisa/', views.resultado_pesquisa, name='resultado-pesquisa')
=======
    # path('resultado-pesquisa/', views.resultado_pesquisa, name='resultado-pesquisa'),
>>>>>>> a23f358e5d9236e35e0aa28aef30dde921d80df4
    # path('<int:glossario_id>/enviar-glossario/', views.enviar_glossario, name='enviar-glossario')
]