# este archivo fue creado manualmente
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
]

# COMENTARIO DE RAMA NUEVO
# este comentario fue hecho solo para la rama 