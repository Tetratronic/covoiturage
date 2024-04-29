from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Trajet
from django import forms

class SignUpForm(UserCreationForm):
    email = forms.EmailField(label="", widget=forms.EmailInput(attrs={'class':'form-control', 'placeholder':'Email'}))
    first_name = forms.CharField(label="",max_length="20", widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Prénom'}))
    last_name = forms.CharField(label="",max_length="20", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Nom'}))
    phone_number = forms.CharField(label='',widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Numéro de téléphone'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name',  'phone_number', 'password1', 'password2')


    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'Nom d\'utilisateur'
        self.fields['username'].label = ''
        self.fields['username'].help_text = ''  

        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['placeholder'] = 'Mot de passe'
        self.fields['password1'].label = ''

        self.fields['password1'].help_text = ''  

        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirmer le mot de passe'
        self.fields['password2'].label = ''
        self.fields['password2'].help_text = ''  
        


class AddTrajetForm(forms.ModelForm):
    class Meta:
        model = Trajet
        fields = ['origin_city', 'destination_city', 'departure_date', 'departure_time', 'available_seats', 'price', 'phone_number', 'car_model']
        labels = {
                "origin_city": "",
                "destination_city": "",
                "departure_date": "",
                "departure_time": "",
                "available_seats": "",
                "price": "",
                "phone_number": "",
                "car_model": "",
            }
        widgets = {
            'origin_city': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Ville de Départ'}),
            'destination_city': forms.TextInput(attrs={'class':'form-control', 'placeholder':' Ville d\'Arrivée'}),
            'departure_date': forms.DateInput(attrs={'class':'form-control', 'placeholder':'Date', 'type':'date'}),
            'departure_time': forms.TimeInput(attrs={'class':'form-control', 'placeholder':'Heure', 'type':'time'}),
            'available_seats': forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Nombre de places'}),
            'price': forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Prix'}),
            'phone_number': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Numéro de téléphone'}),
            'car_model': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Modèle du véhicule'}),	
        }