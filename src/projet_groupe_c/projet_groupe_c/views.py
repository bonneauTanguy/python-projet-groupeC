from django.shortcuts import render
import requests
from datetime import date
import logging


# Create your views here.

from django.http import HttpResponse, HttpRequest
from django.contrib.auth.models import User
from .models import Item
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

logger = logging.getLogger(__name__)


def index(request):
    logger.info("Accès à la vue index")
    return render(request, "home.html")


def register(request):
    logger.info("Accès à la vue register")
    return render(request, "register.html")


def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(username=username, password=password)
        logger.info(f"Tentative de connexion de l'utilisateur {username}")
        if user is not None:
            login(request, user)
            print("je suis dans le if user")
            return redirect(
                "home.html"
            )  # Redirigez vers la page d'accueil après la connexion réussie
    return render(request, "login.html")


def registration_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            logger.info("Nouvel utilisateur enregistré")
            return redirect(
                "login", permanent=True
            )  # Redirigez vers la page de connexion après l'inscription réussie
        else:
            logger.error(f"Erreurs de formulaire d'inscription: {form.errors}")

    else:
        form = UserCreationForm()

    return render(request, "register.html", {"form": form})


def logout(request):
    logger.info("Utilisateur déconnecté")
    return render(request, "logout.html")


def create_item(request):
    if request.method == "POST":
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
        logger.info(f"Nouvel item créé par l'utilisateur {user.username}")
        return render(request, "create_item.html")
    return render(request, "create_item.html", context={})


def item_list(request):
    items = Item.objects.filter(user=request.user)
    logger.info(f"Accès à la vue item_list par l'utilisateur {request.user.username}")
    return render(request, "item_list.html", {"items": items})


@login_required
def changed_mind(request):
    if request.method == "POST":
        new_username = request.POST["new_username"]
        if new_username != request.user.username:
            if User.objects.filter(username=new_username).exists():
                error_message = "Ce nom d'utilisateur est déjà utilisé. Veuillez en choisir un autre."
                logger.warning(
                    "Tentative de modification du nom d'utilisateur échouée : nom d'utilisateur déjà utilisé."
                )
            else:
                request.user.username = new_username
                request.user.save()
                success_message = "Votre nom d'utilisateur a été modifié avec succès."
                logger.info("Nom d'utilisateur modifié avec succès.")
        else:
            error_message = (
                "Veuillez entrer un nom d'utilisateur différent de celui actuel."
            )
            logger.warning(
                "Tentative de modification du nom d'utilisateur échouée : même nom d'utilisateur."
            )
    return render(request, "username_modification.html")
