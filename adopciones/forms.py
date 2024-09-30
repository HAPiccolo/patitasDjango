from django import forms
from core.models import Adopciones, Adoptante


class nuevaAdopcionForm(forms.ModelForm):
    class Meta:
        model = Adopciones
        fields = ["adoptante", "mascota"]

        widgets = {
            "adoptante": forms.Select(attrs={"class": "form-select mt-2"}),
            "mascota": forms.Select(attrs={"class": "form-select mt-2"}),
        }


class adoptanteForm(forms.ModelForm):
    class Meta:
        model = Adoptante
        fields = ["nombre", "apellido", "telefono", "direccion", "edad", "dni"]

        widgets = {
            "nombre": forms.TextInput(attrs={"class": "form-control mt-2"}),
            "apellido": forms.TextInput(attrs={"class": "form-control mt-2"}),
            "telefono": forms.TextInput(attrs={"class": "form-control mt-2"}),
            "direccion": forms.TextInput(attrs={"class": "form-control mt-2"}),
            "edad": forms.TextInput(attrs={"class": "form-control mt-2"}),
            "dni": forms.TextInput(attrs={"class": "form-control mt-2"}),
        }
