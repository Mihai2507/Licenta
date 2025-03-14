from django.db import models
from django.contrib.auth.models import User

class Car(models.Model):
    TIP_CAROSERIE_CHOICES = [
        ('Sedan', 'Sedan'),
        ('Hatchback', 'Hatchback'),
        ('SUV', 'SUV'),
        ('Coupe', 'Coupe'),
        ('Cabrio', 'Cabrio'),
        ('Pickup', 'Pickup'),
        ('Van', 'Van'),
        ('Break', 'Break'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE) # Adaugă un câmp pentru utilizator
    marca = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    an = models.IntegerField()
    kilometri = models.IntegerField()
    pret = models.DecimalField(max_digits=10, decimal_places=2)
    tip_caroserie = models.CharField(max_length=20, choices=TIP_CAROSERIE_CHOICES, default='Sedan')
    descriere = models.TextField()
    imagine = models.ImageField(upload_to='masini/', null=True, blank=True)
    putere_motor = models.IntegerField(help_text="Puterea motorului în CP", null=True, blank=True)
    capacitate_motor = models.IntegerField(help_text="Capacitatea motorului în cm³", null=True, blank=True)

    class Meta:
        db_table = 'car_sale'

    def __str__(self):
        return f"{self.marca} {self.model} - {self.an}"
