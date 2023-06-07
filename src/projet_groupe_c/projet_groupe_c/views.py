from django.shortcuts import render
from django.http import HttpRequest

# Create your views here.
def index(request):
    return render(request, 'home.html')

def register(request):
    return render(request, 'register.html')

def login(request):
    return render(request, 'login.html')

def logout(request):
    return render(request, 'logout.html')