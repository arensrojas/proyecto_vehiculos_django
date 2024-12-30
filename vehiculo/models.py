# vehiculo/models.py
from django.db import models
from django.contrib.auth.models import User, Permission  # Importar User y Permission
from django.contrib.contenttypes.models import ContentType  # Importar ContentType
from django.db.models.signals import post_save
from django.dispatch import receiver

# Definir el modelo Vehiculo
class Vehiculo(models.Model):
    marca = models.CharField(max_length=20, default='Ford')
    modelo = models.CharField(max_length=100)
    serial_carroceria = models.CharField(max_length=50)
    serial_motor = models.CharField(max_length=50)
    categoria = models.CharField(max_length=20, default='Particular')
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.marca} {self.modelo}"

# Crear el permiso 'visualizar_catalogo'
def create_visualizar_catalogo_permission():
    # Obtener el ContentType para el modelo Vehiculo
    content_type = ContentType.objects.get_for_model(Vehiculo)
    
    # Crear el permiso 'visualizar_catalogo' para el modelo Vehiculo
    permission, created = Permission.objects.get_or_create(
        codename='visualizar_catalogo',  # Código del permiso
        name='Puede ver el catálogo de vehículos',  # Nombre del permiso
        content_type=content_type  # Asociar el permiso con el ContentType de Vehiculo
    )
    return permission

# Asignar automáticamente el permiso 'visualizar_catalogo' al registrar un nuevo usuario
@receiver(post_save, sender=User)
def asignar_permiso_al_registro(sender, instance, created, **kwargs):
    if created:
        # Crear y asignar el permiso 'visualizar_catalogo' al nuevo usuario
        permiso = create_visualizar_catalogo_permission()
        instance.user_permissions.add(permiso)
