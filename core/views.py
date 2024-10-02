from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from ingresos.forms import MascotasForm
from .models import Mascotas
# Create your views here.


# comprueva si es super user
def es_superuser(user):
    return user.is_superuser


def home(request):
    mascotas = Mascotas.objects.all()

    return render(request, "core/home.html", {"mascotas": mascotas})


def login(request):
    return render(request, "login.html")


@login_required()
def administracion(request):
    cantMascotas = Mascotas.objects.all().count()
    caninos = Mascotas.objects.filter(especie="canino").count()
    canMacho = Mascotas.objects.filter(especie="canino", sexo="macho").count()
    canHembra = Mascotas.objects.filter(especie="canino", sexo="hembra").count()

    felinos = Mascotas.objects.filter(especie="felino").count()
    felMacho = Mascotas.objects.filter(especie="felino", sexo="macho").count()
    felHembra = Mascotas.objects.filter(especie="felino", sexo="hembra").count()

    context = {
        "cantMascotas": cantMascotas,
        "caninos": caninos,
        "felinos": felinos,
        "canMacho": canMacho,
        "canHembra": canHembra,
        "felMacho": felMacho,
        "felHembra": felHembra,
    }

    return render(request, "core/admin.html", context)
