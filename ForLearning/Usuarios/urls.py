from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
	path('registrar-usuario/', views.registrar_usuario, name="registrar_usuario"),
    path('login/',views.logar, name="login"),
    path('logout/',  auth_views.logout, name="logout")
]
