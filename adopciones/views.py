from django.shortcuts import render, redirect
from .forms import nuevaAdopcionForm, adoptanteForm
# Create your views here.


def nuevaAdopcion(request):
    if request.method == "POST":
        formAdopcion = nuevaAdopcionForm(request.POST)
        if formAdopcion.is_valid():
            adopcion = formAdopcion.save(commit=False)  # No guarda los datos aun
            mascota = adopcion.mascota
            mascota.estado = False
            mascota.save()
            adopcion.save()
            return redirect("administracion")
    else:
        formAdopcion = nuevaAdopcionForm()

    context = {"formAdopcion": formAdopcion}

    return render(request, "nuevaAdopcion.html", context)


def agregarAdoptante(request):
    if request.method == "POST":
        formAdoptante = adoptanteForm(request.POST)
        if formAdoptante.is_valid():
            formAdoptante.save()
            return redirect("nuevaAdopcion")
    else:
        formAdoptante = adoptanteForm()

    context = {"formAdoptante": formAdoptante}

    return render(request, "agregarAdoptante.html", context)
