from django.shortcuts import render
import requests


# Create your views here.

from django.http import HttpResponse, HttpRequest
from .models import item


def create_item(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        url = request.POST.get("url")

        item_object = Item.objects.create(
            username=username,
            password=password,
            url=url,
        )
        item_object.save()

        return render(request, "item_list.html")
    return render(request, "create_item.html", context={})


def item_list(request):
    return render(request, "item_list.html")
