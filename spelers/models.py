from django.db import models

# Create your models here.
class Speler(models.Model):
    naam = models.CharField(max_length=25)
    voorNaam = models.CharField(max_length=15)
    email = models.EmailField(max_length=30)

class Match(models.Model):
    SpelerID = models.IntegerField(default=0)
    punten = models.IntegerField(default=0)
    matchCode = models.IntegerField(default=0)