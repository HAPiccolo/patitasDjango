from django.contrib import admin
from django.urls import path, include
from core.views import *
from debug_toolbar.toolbar import debug_toolbar_urls

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", home, name="home"),
    path("login/", include("login.urls")),
    path("administracion/", administracion, name="administracion"),
] + debug_toolbar_urls()
