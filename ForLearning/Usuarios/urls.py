from django.urls import path
from . import views

urlpatterns = [
	path('registrar/', views.registrar, name="registrar"),
    path('login/',views.logar, name="login"),
	# path(r'^logout/$', 'django.contrib.auth.views.logout_then_login', {'login_url': '/login'}, name="logout")
]
