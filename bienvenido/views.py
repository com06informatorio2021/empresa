from django.shortcuts import render, HttpResponse
from bienvenido.models import Departamento

# Create your views here.
def bienvenido(request):
    return HttpResponse("<h1>Hola Mundo</h1>")

def inicio(request):
    template = "bienvenido/index.html"
    contexto = {}
    return render(request, template, contexto)

def departamentos(request):
    dptos = Departamento.objects.all()
    template = "bienvenido/departamentos.html"
    contexto = {
        "lista_departamentos":dptos
    }
    return render(request, template, contexto)