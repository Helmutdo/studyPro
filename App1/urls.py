# este archivo fue creado manualmente
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
]

# COMENTARIO DE RAMA NUEVO
# este comentario fue hecho solo para la rama 