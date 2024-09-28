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
            "foto": forms.FileInput(attrs={"enctype": "multipart/form-data"}),
        }
