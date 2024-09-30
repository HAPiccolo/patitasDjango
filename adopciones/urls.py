from django.urls import path
from .views import nuevaAdopcion, agregarAdoptante

urlpatterns = [
    path("nuevaAdopcion/", nuevaAdopcion, name="nuevaAdopcion"),
    path("agregarAdoptante/", agregarAdoptante, name="agregarAdoptante"),
]
