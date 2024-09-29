from django.contrib import admin
from django.urls import path, include
from .views import home, administracion
from debug_toolbar.toolbar import debug_toolbar_urls
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", home, name="home"),
    path("login/", include("login.urls")),
    path("ingresos/", include("ingresos.urls")),
    path("administracion/", administracion, name="administracion"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += debug_toolbar_urls()
