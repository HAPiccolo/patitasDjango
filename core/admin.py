from django.contrib import admin
from .models import Adoptante, Adopciones, Mascotas


class MascotasAdmin(admin.ModelAdmin):
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
admin.site.register(Mascotas, MascotasAdmin)
admin.site.register(Adoptante)
admin.site.register(Adopciones)
