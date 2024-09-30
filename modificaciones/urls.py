from django.urls import path
from .views import editarMascota, modificarMascota

urlpatterns = [
    path("editarMascota", editarMascota, name="editarMascota"),
    path("modificarMascota/<int:id>", modificarMascota, name="modificarMascota"),
]
