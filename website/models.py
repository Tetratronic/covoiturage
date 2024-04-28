from django.db import models

# Modeliser les Trajets dans la base de données

class Trajet(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    first_name = models.CharField(max_length=50)              #nom
    last_name = models.CharField(max_length=50)               #prenom
    origin_city = models.CharField(max_length=100)            #ville de depart
    destination_city = models.CharField(max_length=100)       #destination
    departure_date = models.DateField(max_length=50)          #date de depart
    available_seats = models.CharField(max_length=50)         #places disponibles
    price = models.PositiveSmallIntegerField()                #prix par place
    phone_number = models.CharField(max_length=50)            #numero de telephone
    car_model = models.CharField(max_length=50)               #Modele de la voiture

    def __str__(self) -> str:
        return(f"{self.first_name}{self.last_name}")
