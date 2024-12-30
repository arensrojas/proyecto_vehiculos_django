
from django.db import models
from django.shortcuts import render, redirect
from .forms import VehiculoForm, Vehiculo
from django.contrib.auth.decorators import login_required, permission_required

# Create your views here.

# vehiculo/views.py


def index(request):
    return render(request, 'index.html')  # Renderiza la página de inicio

def agregar_vehiculo(request):
    if request.method == 'POST':
        form = VehiculoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')  # Redirige a la página de inicio después de guardar el vehículo
    else:
        form = VehiculoForm()
    return render(request, 'agregar_vehiculo.html', {'form': form})


# def listar_vehiculos(request):
#    return render(request, 'index.html')

@login_required
@permission_required('vehiculo.visualizar_catalogo', raise_exception=True)# verifica el permiso
def listar_vehiculos(request):
    # Obtener todos los vehículos de la base de datos
    vehiculos = Vehiculo.objects.all()
    
    # Filtrar los vehículos por rango de precios (opcional)
    precio_bajo = vehiculos.filter(precio__lte=10000)
    precio_medio = vehiculos.filter(precio__gt=10000, precio__lte=30000)
    precio_alto = vehiculos.filter(precio__gt=30000)

    # Pasar los vehículos a la plantilla
    return render(request, 'vehiculo/listar_vehiculos.html', {
        'vehiculos': vehiculos,
        'precio_bajo': precio_bajo,
        'precio_medio': precio_medio,
        'precio_alto': precio_alto,
    })






