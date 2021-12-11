from django import forms
from django.db.models import fields
from bienvenido.models import Departamento

class FiltroDptos(forms.Form):
    nombre = forms.CharField(max_length=50, required=False)
    numero = forms.IntegerField(required=False)

class DepartamentoForm(forms.ModelForm):
    class Meta:
        model = Departamento
        fields = ("nombre",)