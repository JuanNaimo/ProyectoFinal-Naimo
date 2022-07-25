from django import forms
from dataclasses import fields
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class EquipoFormulario(forms.Form):

    nombre= forms.CharField(max_length=60)
    liga= forms.CharField(max_length=50)
    pais= forms.CharField(max_length=20)
    division= forms.CharField(max_length=20)
    edad= forms.IntegerField()
    estadio= forms.CharField(max_length=40)

class JugadorFormulario(forms.Form):

    nombre= forms.CharField(max_length=30)
    apellido= forms.CharField(max_length=20)
    posicion= forms.CharField(max_length=20)
    pie= forms.CharField(max_length=12)
    edad= forms.IntegerField()
    club= forms.CharField(max_length=30)
    dorsal= forms.IntegerField()

class EntrenadorFormulario(forms.Form):
    
    nombre= forms.CharField(max_length=30)
    apellido= forms.CharField(max_length=20)
    edad= forms.IntegerField()
    club= forms.CharField(max_length=30)
    exjug= forms.BooleanField()
    