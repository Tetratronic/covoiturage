from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm, AddTrajetForm, UpdateUserForm, UpdateProfileForm
from django.contrib.auth.decorators import login_required
from .models import Trajet
from django.urls import reverse_lazy
from django.contrib.auth.views import PasswordChangeView
from django.contrib.messages.views import SuccessMessageMixin

# page d'acceuil
def home(request):  
    trajets = Trajet.objects.order_by('-created_at')[:10] #Afficher les 10 premiers trajets
    return render(request, 'home.html' ,{'user': request.user, 'trajets':trajets})

def login_user(request):
    #connecter un utilisateur 
    
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
    return redirect('home')

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

def add_trajet(request):
        if request.method == 'POST':
             form = AddTrajetForm(request.POST)
             if form.is_valid():
                Trajet = form.save(commit=False)
                Trajet.user= request.user
                Trajet.save()
                messages.success(request, "Opération réussie")
                return redirect('home')
        else:
            form = AddTrajetForm()
        return render(request, 'add-trajet.html', {'form':form})
    


# Fonction pour Supprimer un trajet
def delete_trajet(request, pk):
     trajet = Trajet.objects.get(id=pk)
     user = request.user
     if user.first_name == trajet.first_name:
        trajet.delete
        return redirect('home')
     else:
         messages.success(request,"Non autorisé")
         return redirect('home')


@login_required
def profile(request):
    if request.method == 'POST':
        user_form = UpdateUserForm(request.POST, instance=request.user)
        profile_form = UpdateProfileForm(request.POST, request.FILES, instance=request.user.profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Profil mis a jour avec succes !')
            return redirect(to='users-profile')
    else:
        user_form = UpdateUserForm(instance=request.user)
        profile_form = UpdateProfileForm(instance=request.user.profile)

    return render(request, 'profile.html', {'user_form': user_form, 'profile_form': profile_form})


class ChangePasswordView(SuccessMessageMixin, PasswordChangeView):
    template_name = 'change_password.html'
    success_message = "Mot de passe changé avec succes"
    success_url = reverse_lazy('home')