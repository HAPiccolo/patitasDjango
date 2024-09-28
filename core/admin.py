from django.contrib import admin
from .models import Caracteristicas, Adoptante, Adopciones


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
admin.site.register(Adopciones)
