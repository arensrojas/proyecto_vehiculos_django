"""
URL configuration for proyecto_vehiculos_django project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# proyecto_vehiculos_django/urls.py
from django.contrib import admin
from django.urls import path, include  # Incluye la función `include` para incluir las URLs de la aplicación
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),  # Ruta para el sitio de administración
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),  # Vista de Login
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),  # Vista de Logout
    path('', include('vehiculo.urls')),  # Incluye las URLs de la aplicación 'vehiculo'
    
]


