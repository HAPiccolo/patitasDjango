from django.http import JsonResponse
from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth import authenticate, login
from ingresos.forms import MascotasForm, FiltroMascotaFrom
from .models import Caracteristicas
# Create your views here.


# comprueva si es super user
def es_superuser(user):
    return user.is_superuser


def home(request):
    return render(request, "core/home.html")


def login(request):
    return render(request, "login.html")


@login_required()
def administracion(request):
    if request.method == "POST":
        mascotaForm = MascotasForm(request.POST)
        if mascotaForm.is_valid():
            mascotaForm.save()
            return redirect(
                "administracion"
            )  # Fix hasta solucionar la limpieza de campos
            messages.success(request, "Se ingresaron correctamente los datos.")

        else:
            messages.error(request, "Hubo un error en el formulario.")
    else:
        mascotaForm = MascotasForm()
        filtro = FiltroMascotaFrom()

    context = {"mascotasForm": mascotaForm}
    return render(request, "core/admin.html", context)
