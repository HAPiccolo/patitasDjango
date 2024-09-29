from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import MascotasForm
# Create your views here.


@login_required()
def ingresoMascota(request):
    if request.method == "POST":
        mascotaForm = MascotasForm(request.POST, request.FILES)
        if mascotaForm.is_valid():
            mascotaForm.save()
            return redirect(
                "administracion"
            )  # Fix hasta solucionar la limpieza de campos
            messages.success(request, "Se ingresaron correctamente los datos.")

    else:
        mascotaForm = MascotasForm()

    context = {"mascotasForm": mascotaForm}

    return render(request, "ingresoMascota.html", context)
