from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, render
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm, UserCreationForm, PasswordChangeForm
# Create your views here.
from django.contrib.auth.models import User
from perfil.forms import EditarUsuarioForm, NuevoUsuarioForm

def iniciar_sesion(request):
    form = AuthenticationForm(data = request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request,user)
                return redirect("inicio")
    return render(request, "perfil/login.html",{
        "form":form,
    })

def cerrar_sesion(request):
    logout(request)
    return redirect("inicio")

def nuevo_usuario(request):
    if request.user.is_authenticated:
        return redirect("inicio")

    form = NuevoUsuarioForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            user = form.save()
            #user.set_password("clave1234")
            if user is not None:
                login(request,user)
                return redirect("inicio")
    return render(request, "perfil/nuevo_usuario.html", {
        "form":form
    })


def editar_usuario(request):
    if not request.user.is_authenticated:
        return redirect("login")
    user = request.user
    form = EditarUsuarioForm(request.POST or None, instance=user)
    if request.method == "POST":
        if form.is_valid():
            user = form.save()
            return redirect("inicio")
    return render(request, "perfil/editar_usuario.html",{
        "form":form,
    })

def editar_clave(request):
    if not request.user.is_authenticated:
        return redirect("login")
    user = request.user
    form = PasswordChangeForm(data=request.POST or None, user=user)
    if request.method == "POST":
        if form.is_valid():
            user = form.save()
            return redirect("inicio")
    return render(request, "perfil/editar_clave.html",{
        "form":form,
    })
