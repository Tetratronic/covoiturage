from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save  
# Modeliser les Trajets dans la base de données

class Trajet(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE)  #Posteur du trajet
    last_name = models.CharField(max_length=50)               #prenom
    origin_city = models.CharField(max_length=100)            #ville de depart
    destination_city = models.CharField(max_length=100)       #destination
    departure_date = models.DateField(max_length=50)          #date de depart
    departure_time = models.TimeField(default="08:30")
    available_seats = models.CharField(max_length=50)         #places disponibles
    price = models.PositiveSmallIntegerField()                #prix par place
    phone_number = models.CharField(max_length=50)            #numero de telephone
    car_model = models.CharField(max_length=50)               #Modele de la voiture

    def __str__(self) -> str:
        return(f"{self.origin_city}{self.destination_city}")




class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    profile_pic = models.ImageField(default='default.jpg', upload_to='profile_images')


    def __str__(self):
        return self.user.username