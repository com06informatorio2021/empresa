"""empresa URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
from bienvenido import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('bienvenido/', views.bienvenido),
    path('', views.inicio, name="inicio"),
    path('departamentos/', views.departamentos, name="departamentos"),
    path('departamentos/<int:id>/', views.ver_dpto, name="ver_dpto"),
    # ver dpto
    # crear dpto
    # editar dpto
    path('departamentos/nuevo/', views.nuevo_dpto, name="nuevo_dpto"),
    path('departamentos/<int:id>/editar/', views.editar_dpto, name="editar_dpto"),
    path('departamentos/<int:id>/borrar/', views.borrar_dpto, name="borrar_dpto"),
    # eliminar dpto
    
    # listar empleados
    path ('empleados/lista/', views.lista_empleados, name="lista_empleados"),
    # ver empleado
    path ('empleados/<int:id>/', views.ver_empleado, name="ver_empleado"),
    
    # crear empleado
    path ('empleados/nuevo/', views.nuevo_empleado, name="nuevo_empleado"),
    # editar empleado
    # eliminar empleado
    path("perfil/", include("perfil.urls")),
]
