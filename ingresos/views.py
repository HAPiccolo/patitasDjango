from django.shortcuts import render

# Create your views here.


def ingresoMascota(request):
    return render(request, "ingresoMascota.html")
