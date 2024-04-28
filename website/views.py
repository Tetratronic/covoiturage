from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm
from .models import Trajet
# page d'acceuil
def home(request):
    #connecter un utilisateur 

    trajets = Trajet.objects.all()

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username = username, password = password)
        if user:
            login(request, user)
            messages.success(request,"Connexion réussie")
            return redirect('home')
        else:
            messages.success(request, "Erreur, Reessayer")
        
    return render(request, 'home.html', {'trajets': trajets})

#fonction pour se déconnecter
def logout_user(request):
    logout(request)
    messages.success(request, "Déconnexion réussie !")
    return redirect('home')

def register_user(request):
    if request.method == 'POST':
             form = SignUpForm(request.POST)
             if form.is_valid():
                form.save()
                username = form.cleaned_data['username']
                password = form.cleaned_data['password1']
                user = authenticate(username=username, password=password)
                login(request, user)
                messages.success(request, "Inscription réussie")
                return redirect('home')
    else:
         form = SignUpForm()
    return render(request, 'register.html', {'form':form})