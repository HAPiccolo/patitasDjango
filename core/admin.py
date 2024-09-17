from django.contrib import admin
from .models import Caracteristicas, Adoptante, Empleado, Mascota, Adopciones


class CaracteristicasAdmin(admin.ModelAdmin):
    list_display = (
        "edad",
        "discapacidad",
        "raza",
        "sexo",
        "especie",
        "nombre",
        "fecha_ingreso",
        "foto",
    )


# Register your models here.
admin.site.register(Caracteristicas, CaracteristicasAdmin)
admin.site.register(Adoptante)
admin.site.register(Empleado)
admin.site.register(Mascota)
admin.site.register(Adopciones)
