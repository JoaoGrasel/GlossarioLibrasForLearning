from django.urls import path
from . import views

urlpatterns = [
	path('registrar/', views.registrar_usuario_view, name="registrar"),
    path('login/',views.login_view, name="login"),
	# path(r'^logout/$', 'django.contrib.auth.views.logout_then_login', {'login_url': '/login'}, name="logout")
]
