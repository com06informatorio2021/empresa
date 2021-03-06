from django.urls import path
from perfil import views
#from django.contrib.auth import views as auth_views

urlpatterns = [
    #path("", ) mi perfil
    path("login/",views.iniciar_sesion,name="login"),
    path("logout/",views.cerrar_sesion,name="logout"),
    # registrar usuarios
    path("nuevo/", views.nuevo_usuario, name="nuevo_usuario"),
    # editar perfil
    path("editar/", views.editar_usuario, name="editar_usuario"),
    # cambiar clave
    path("editar-clave/", views.editar_clave, name="editar_clave"),
]
