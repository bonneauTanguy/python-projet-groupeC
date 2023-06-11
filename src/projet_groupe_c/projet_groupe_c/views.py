from django.shortcuts import render
import requests
from datetime import date


# Create your views here.

from django.http import HttpResponse, HttpRequest
from django.contrib.auth.models import User
from .models import Item
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm

from .forms import PasswordForm


def index(request):
    return render(request, "home.html")


def register(request):
    return render(request, "register.html")


def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(username=username, password=password)
        print("juste avant")
        if user is not None:
            login(request, user)
            print("je suis dans le if user")
            return redirect(
                "/"
            )  # Redirigez vers la page d'accueil après la connexion réussie
    return render(request, "login.html")


def registration_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(
                "login", permanent=True
            )  # Redirigez vers la page de connexion après l'inscription réussie
        else:
            print(
                form.errors
            )  # Afficher les erreurs du formulaire dans la console Python

    else:
        form = UserCreationForm()

    return render(request, "register.html", {"form": form})


def logout(request):
    return render(request, "logout.html")


def create_item(request):
    if request.method == "POST":
        form = PasswordForm(request.POST)
        if form.is_valid():
            username = request.POST.get("username")
            password = request.POST.get("password")
            url = request.POST.get("url")
            user = request.user

            item_object = Item.objects.create(
                username=username,
                password=password,
                url=url,
                creation_date=date.today(),
                user=user,
            )
            item_object.save()

            return redirect("item_created")
    else:
        form = PasswordForm()

    return render(request, "create_item.html", {"form": form})


def item_list(request):
    items = Item.objects.filter(user=request.user)
    return render(request, "item_list.html", {"items": items})


def change_password(request):
    if request.method == 'POST':
        form = PasswordForm(request.POST)
        if form.is_valid():
            # Le mot de passe est valide et a passé la vérification du score
            # Effectuez ici les actions nécessaires, telles que la mise à jour du mot de passe dans la base de données
            return render(request, 'password_change_success.html')
    else:
        form = PasswordForm()
    
    return render(request, 'change_password.html', {'form': form})
