from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def index(request):
    return render(request, 'home.html')


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home.html')  # Redirigez vers la page d'accueil après la connexion réussie
    return render(request, 'login.html')

def registration_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Redirigez vers la page de connexion après l'inscription réussie
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

def logout(request):
    return render(request, 'logout.html')