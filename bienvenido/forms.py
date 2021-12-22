from django import forms
from django.db.models import fields
from bienvenido.models import Departamento, Empleado


class FiltroDptos(forms.Form):
    nombre = forms.CharField(max_length=50, required=False)
    numero = forms.IntegerField(required=False)

class FiltroEmpleado(forms.Form):
    nombre = forms.CharField(max_length=50, required=False)
    apellido = forms.CharField(max_length=50, required=False)
    sueldo_min = forms.DecimalField(required=False)
    sueldo_max = forms.DecimalField(required=False)
    departamento = forms.ModelChoiceField(Departamento.objects.all(), required=False)


class DepartamentoForm(forms.ModelForm):
    class Meta:
        model = Departamento
        fields = ("nombre",)
    

class EmpleadoForm(forms.ModelForm):
    class Meta:
        model = Empleado
        fields = ("__all__")