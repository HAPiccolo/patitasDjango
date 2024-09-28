from django.urls import path
from .views import ingresoMascota

urlpatterns = [
    path("ingresoMascota", ingresoMascota, name="ingresoMascota"),
]
