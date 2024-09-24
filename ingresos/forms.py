from django import forms

from core.models import Caracteristicas


class MascotasForm(forms.ModelForm):
    class Meta:
        model = Caracteristicas
        fields = [
            "nombre",
            "edad",
            "raza",
            "sexo",
            "especie",
            "discapacidad",
            "foto",
        ]
        widgets = {
            "nombre": forms.TextInput(attrs={"class": "form-control mt-2"}),
            "edad": forms.NumberInput(attrs={"class": "form-control mt-2"}),
            "raza": forms.TextInput(attrs={"class": "form-control mt-2"}),
            "discapacidad": forms.Textarea(attrs={"class": "form-control mt-2"}),
            "sexo": forms.Select(attrs={"class": "form-select mt-2"}),
            "especie": forms.Select(attrs={"class": "form-select mt-2"}),
        }

    def clean(self):
        cleaned_data = super().clean()
        nombre = cleaned_data.get("nombre")

        if nombre:
            try:
                mascota = Caracteristicas.objects.get(nombre=nombre)
                cleaned_data.update(
                    mascota.__dict__
                )  # Update form data with fetched data
            except Caracteristicas.DoesNotExist:
                self.add_error("nombre", "La mascota no existe.")

        return cleaned_data


class FiltroMascotaFrom(forms.ModelForm):
    class Meta:
        model = Caracteristicas
        fields = [
            "nombre",
        ]

        widgets = {
            "nombre": forms.TextInput(attrs={"class": "form-control mt-2"}),
        }
