from django.db import models


# Create your models here.


class Adoptante(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    telefono = models.CharField(max_length=20)
    direccion = models.CharField(max_length=200)
    edad = models.CharField(max_length=2)
    dni = models.CharField(max_length=10, primary_key=True, null=False)


class Caracteristicas(models.Model):
    edad = models.CharField(max_length=2)
    discapacidad = models.CharField(max_length=500, null=True, blank=True)
    raza = models.CharField(max_length=50)
    sexo = models.CharField(
        max_length=10,
        choices=[("macho", "Macho"), ("hembra", "Hembra")],
        default="Macho",
    )
    especie = models.CharField(
        max_length=50,
        choices=[("canino", "Canino"), ("felino", "Felino")],
        default="Canino",
    )
    nombre = models.CharField(max_length=50)
    fecha_ingreso = models.DateField()
    foto = models.ImageField(null=True, blank=True)


class Empleado(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    direccion = models.CharField(max_length=200)
    telefono = models.CharField(max_length=20)
    dni = models.CharField(max_length=10, primary_key=True, null=False)


class Mascota(models.Model):
    adoptante = models.ForeignKey(Adoptante, on_delete=models.CASCADE)
    empleado = models.ForeignKey(Empleado, on_delete=models.CASCADE)
    masco = models.ForeignKey(Caracteristicas, on_delete=models.CASCADE)


class Adopciones(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    telefono = models.CharField(max_length=20)
    direccion = models.CharField(max_length=200)
    edad = models.CharField(max_length=2)
    dni = models.CharField(max_length=10, primary_key=True, null=False)
    mascota = models.ForeignKey(Caracteristicas, on_delete=models.CASCADE)
    fecha_adopcion = models.DateField()
