
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('Glossario/', include('Glossario.urls')),
    path('', include('Glossario.urls')),
]
