from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from core.models import Mascotas
from .forms import ModificarMascotasForm
# Create your views here.


# Muestra un listado de las mascotas
@login_required()
def editarMascota(request):
    mascotas = Mascotas.objects.all()

    context = {"mascotas": mascotas}

    return render(request, "listado.html", context)


# Lleva al formulario para la edicion de la mascota


@login_required()
def modificarMascota(request, id):
    # obtenemos el id de la mascota seleccionada en la tabla
    mascota = Mascotas.objects.get(id=id)
    if request.method == "POST":
        formulario = ModificarMascotasForm(request.POST, instance=mascota)
        if formulario.is_valid():
            formulario.save()
            return redirect("editarMascota")
    else:
        formulario = ModificarMascotasForm(instance=mascota)

    context = {"formulario": formulario}
    return render(request, "modificarMascota.html", context)
