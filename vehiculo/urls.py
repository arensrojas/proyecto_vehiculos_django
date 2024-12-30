# vehiculo/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # Página de inicio
    path('vehiculo/add/', views.agregar_vehiculo, name='agregar_vehiculo'),  # Formulario para agregar vehículo
    path('vehiculo/list/', views.listar_vehiculos, name ='listar_vehiculos'),
]
