from django.shortcuts import render
import requests
from datetime import date


# Create your views here.

from django.http import HttpResponse, HttpRequest
from django.contrib.auth.models import User
from .models import Item


def create_item(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        url = request.POST.get("url")
        user = request.user

        utilisateur = User.objects.get()
        item_object = Item.objects.create(
            username=username,
            password=password,
            url=url,
            creation_date=date.today(),
            user=user,
        )
        item_object.save()

        return render(request, "create_item.html")
    return render(request, "create_item.html", context={})


def item_list(request):
    items = Item.objects.filter(user=request.user)
    return render(request, "item_list.html", {"items": items})
