from django.shortcuts import render, redirect
from .forms import nuevaAdopcionForm, adoptanteForm
# Create your views here.


def nuevaAdopcion(request):
    if request.method == "POST":
        formAdopcion = nuevaAdopcionForm(request.POST)
        if formAdopcion.is_valid():
            formAdopcion.save()
            return redirect("")
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
