from django.db import models


# Create your models here.


class Adoptante(models.Model):
    id_adoptate = models.IntegerField(primary_key=True, null=False)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    telefono = models.CharField(max_length=20)
    direccion = models.CharField(max_length=200)
    edad = models.CharField(max_length=2)
    dni = models.CharField(max_length=10)


class Caracteristicas(models.Model):
    id_caracteristica = models.IntegerField(primary_key=True, null=False)
    id_mascota = models.ForeignKey("mascotas", on_delete=models.CASCADE)
    edad = models.CharField(max_length=2)
    discapacidad = models.CharField(max_length=500)
    raza = models.CharField(max_length=50)
    sexo = models.CharField(
        max_length=10,
        choices=[("macho", "Macho"), ("hembra", "Hembra")],
        default="Macho",
    )
    nombre = models.CharField(max_length=50)
    fecha_ingreso = models.DateTimeField()
    foto = models.ImageField()


class Empleado(models.Model):
    id_empleado = models.IntegerField(primary_key=True, null=False)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    direccion = models.CharField(max_length=200)
    telefono = models.CharField(max_length=20)
    dni = models.CharField(max_length=10)


class Especie(models.Model):
    id_especie = models.IntegerField(primary_key=True, null=False)
    especie = models.CharField(max_length=20)


class Mascotas(models.Model):
    id_mascota = models.IntegerField(primary_key=True, null=False)
    id_especie = models.ForeignKey(Especie, on_delete=models.CASCADE)
    id_adopciones = models.ForeignKey("Adopciones", on_delete=models.CASCADE)


class Adopciones(models.Model):
    id_adopciones = models.IntegerField(primary_key=True, null=False)
    id_adoptante = models.ForeignKey(Adoptante, on_delete=models.CASCADE)
    id_empleado = models.ForeignKey(Empleado, on_delete=models.CASCADE)
    id_mascota = models.ForeignKey(Mascotas, on_delete=models.CASCADE)
