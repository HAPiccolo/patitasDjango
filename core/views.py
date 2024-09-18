from django.http import JsonResponse
from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth import authenticate, login
from ingresos.forms import MascotasForm
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
            return JsonResponse(
                {"success": True, "message": "Mascota creada exitosamente"}
            )
        else:
            return JsonResponse({"success": False, "errors": mascotaForm.errors})
            messages.error(request, "Hubo un error en el formulario.")
    else:
        mascotaForm = MascotasForm()

    contenidos = {"mascotasForm": mascotaForm}
    print(contenidos)
    return render(request, "core/admin.html", contenidos)
