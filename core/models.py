from django.db import models


class Adoptante(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    telefono = models.CharField(max_length=20)
    direccion = models.CharField(max_length=200)
    edad = models.CharField(max_length=2)
    dni = models.CharField(max_length=10, primary_key=True, null=False)

    def __str__(self) -> str:
        return f"{self.dni} - {self.nombre} {self.apellido} "


class Mascotas(models.Model):
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
    fecha_ingreso = models.DateField(auto_now_add=True)
    foto = models.ImageField(
        null=True, blank=True, upload_to="images"
    )  # guarda la imagen en media/images/
    estado = models.BooleanField(default=True)

    # retorna el nombre de la mascota
    def __str__(self) -> str:
        return f"{self.nombre}"


class Adopciones(models.Model):
    adoptante = models.ForeignKey(Adoptante, on_delete=models.CASCADE)
    mascota = models.ForeignKey(Mascotas, on_delete=models.CASCADE)
    fecha_adopcion = models.DateField(auto_now_add=True)

    def __str__(self) -> str:
        return f"{self.adoptante} | {self.mascota}"
