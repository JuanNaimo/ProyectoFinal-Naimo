from itertools import pairwise
from statistics import linear_regression
from django.db import models

# Create your models here.

class Equipo(models.Model):
    
    nombre= models.CharField(max_length=60)
    liga= models.CharField(max_length=50)
    pais= models.CharField(max_length=20)
    division= models.CharField(max_length=20)
    edad= models.IntegerField()
    estadio=models.CharField(max_length=40)

class Jugador(models.Model):

    nombre= models.CharField(max_length=30)
    apellido= models.CharField(max_length=20)
    posicion= models.CharField(max_length=20)
    pie= models.CharField(max_length=12)
    edad= models.IntegerField()
    club= models.CharField(max_length=30)
    dorsal= models.IntegerField()

    def __str__(self):
        return f"Nombre: {self.nombre} - Apellido: {self.apellido} - Posicion: {self.posicion} - Pie: {self.pie} - Edad: {self.edad} - Club: {self.club} - Dorsal: {self.dorsal}"

class Entrenador(models.Model):
    
    nombre= models.CharField(max_length=30)
    apellido= models.CharField(max_length=20)
    edad= models.IntegerField()
    club= models.CharField(max_length=30)
    exjug= models.BooleanField()
    