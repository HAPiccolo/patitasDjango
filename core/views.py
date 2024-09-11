from django.shortcuts import render
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth import authenticate, login
# Create your views here.


# comprueva si es super user
def es_superuser(user):
    return user.is_superuser


def home(request):
    return render(request, "core/home.html")


def login(request):
    return render(request, "login.html")
