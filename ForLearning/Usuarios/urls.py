from django.urls import path
from . import views

urlpatterns = [
	path('registrar-usuario/', views.registrar_usuario, name="registrar_usuario"),
    path('login/',views.logar, name="login"),
	# path(r'^logout/$', 'django.contrib.auth.views.logout_then_login', {'login_url': '/login'}, name="logout")
]
