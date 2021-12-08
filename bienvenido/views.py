from django.shortcuts import render, HttpResponse

# Create your views here.
def bienvenido(request):
    return HttpResponse("Hola Mundo")

def inicio(request):
    template = "bienvenido/index.html"
    contexto = {}
    return render(request, template, contexto)