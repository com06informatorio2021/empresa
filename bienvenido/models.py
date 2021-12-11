from django.db import models

# Create your models here.
class Departamento(models.Model):
    nombre = models.CharField(max_length=50, null=False, blank=False, unique=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "Departamento: " + self.nombre


class Empleado(models.Model):
    nombre = models.CharField(max_length=100, null=False, blank=False)
    apellido = models.CharField(max_length=100, null=False, blank=False)
    fecha_nacimiento = models.DateTimeField(default=None)
    sueldo = models.DecimalField(max_digits=10, decimal_places=2, default=10000)
    departamento = models.ForeignKey(Departamento, on_delete=models.SET_NULL, null=True)
    dni = models.CharField(max_length=8, unique=True)
    apodo =  models.CharField(max_length=100, null=False, blank=False, default="sin apodo")

