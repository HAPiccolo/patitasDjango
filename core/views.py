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
    return render(request, "core/admin.html")
