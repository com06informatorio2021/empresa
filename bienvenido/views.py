from django.http.response import Http404
from django.shortcuts import render, HttpResponse, redirect
from bienvenido.models import Departamento, Empleado
from bienvenido.forms import FiltroDptos, DepartamentoForm, EmpleadoForm

# Create your views here.
def bienvenido(request):
    return HttpResponse("<h1>Hola Mundo</h1>")

def inicio(request):
    #import pdb; pdb.set_trace()
    template = "bienvenido/index.html"
    contexto = {}
    return render(request, template, contexto)

def departamentos(request):
    formulario = FiltroDptos(request.GET or None)
    if formulario.is_valid():
        print("formulario valido: ", formulario.cleaned_data)
        filtro_nombre = formulario.cleaned_data["nombre"]
        dptos = Departamento.objects.filter(nombre__contains = filtro_nombre)
    else:
        print(formulario.errors)
        dptos = Departamento.objects.all()
    template = "bienvenido/departamentos.html"
    contexto = {
        "lista_departamentos":dptos,
        "formulario":formulario,
    }
    return render(request, template, contexto)

def ver_dpto(request, id):
    try:
        dpto = Departamento.objects.get(pk=id)
    except:
        raise Http404("no hay ese dpto")

    contexto = {
        "dpto":dpto
    }
    return render(request, "bienvenido/dpto.html", contexto)

def nuevo_dpto(request):
    formulario = DepartamentoForm(request.POST or None)
    print("metodo: ", request.method)
    if request.method == "POST":
        if formulario.is_valid():
            dpto = formulario.save()
            return redirect("ver_dpto", dpto.id)

    template = "bienvenido/nuevo_dpto.html"
    contexto = {
        "formulario":formulario
    }
    return render(request, template, contexto)

def editar_dpto(request, id):
    dpto = Departamento.objects.get(pk=id)
    formulario = DepartamentoForm(request.POST or None, instance=dpto)
    print("metodo: ", request.method)
    if request.method == "POST":
        if formulario.is_valid():
            dpto = formulario.save()
            return redirect("ver_dpto", dpto.id)

    template = "bienvenido/nuevo_dpto.html"
    contexto = {
        "formulario":formulario
    }
    return render(request, template, contexto)

def borrar_dpto(request,id):
    dpto = Departamento.objects.get(pk=id)
    if request.method == "POST":
        dpto.delete()
        return redirect("departamentos")
    return render(request, "bienvenido/borrar_dpto.html", {"dpto":dpto})

def ver_empleado(request, id):
    try:
        empleado = Empleado.objects.get(pk=id)
    except:
        raise Http404("no hay ese Empleado")

    contexto = {
        "empleado":empleado
    }
    return render(request, "bienvenido/empleado.html", contexto)

def nuevo_empleado(request):
    formulario = EmpleadoForm(request.POST or None)
    
    if request.method == "POST":
        if formulario.is_valid():
            empleado = formulario.save()
            return redirect("ver_empleado", empleado.id)

    template = "bienvenido/nuevo_empleado.html"
    contexto = {
        "formulario":formulario
    }
    return render(request, template, contexto)

def lista_empleados(request):
    #formulario = FiltroDptos(request.GET or None)
    #if formulario.is_valid():
    #    print("formulario valido: ", formulario.cleaned_data)
    #    filtro_nombre = formulario.cleaned_data["nombre"]
    #    dptos = Departamento.objects.filter(nombre__contains = filtro_nombre)
    #else:
    #    print(formulario.errors)
    #    dptos = Departamento.objects.all()
    template = "bienvenido/lista_empleados.html"
    contexto = {
        "lista_empleados":Empleado.objects.all(),
        
    }
    return render(request, template, contexto)