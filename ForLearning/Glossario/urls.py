from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:categoria_id>/', views.conteudo_categoria, name='conteudo-categoria'),
    path('<int:categoria_id>/enviar-sinal/', views.enviar_sinal, name='enviar-sinal'),
    path('sinal-enviado-com-sucesso/', views.sinal_enviado_sucesso, name='sinal-enviado-sucesso'),
]