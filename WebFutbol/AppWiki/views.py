from ast import Return
import re
from django.http.request import QueryDict
from django.shortcuts import render, HttpResponse
from django.http import HttpResponse
from AppCuentas.models import Avatar
from AppWiki.models import Jugador, Entrenador, Equipo
from AppWiki.forms import JugadorFormulario, EquipoFormulario, EntrenadorFormulario
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from time import gmtime, strftime
# Create your views here.
def inicio(request):

    avatares=Avatar.objects.filter(user=request.user.id)
    if avatares.exists():
        
        return render(request, "AppWiki/inicio.html", {"url":avatares[0].imagen.url})
    else:
        return render(request, "AppWiki/inicio.html")

def entrenadores(request):

    avatares=Avatar.objects.filter(user=request.user.id)
    if avatares.exists():
        
        return render(request, "AppWiki/entrenadores.html", {"url":avatares[0].imagen.url})
    else:
        return render(request, "AppWiki/entrenadores.html")

def jugadores(request):
    
    avatares=Avatar.objects.filter(user=request.user.id)
    if avatares.exists():
        
        return render(request, "AppWiki/jugadores.html", {"url":avatares[0].imagen.url})
    else:
        return render(request,"AppWiki/jugadores.html")

def equipos(request):

    avatares=Avatar.objects.filter(user=request.user.id)
    if avatares.exists():
        
        return render(request, "AppWiki/equipos.html", {"url":avatares[0].imagen.url})
    else:
        return render(request, "AppWiki/equipos.html")

def agregarentrenadores(request):
    avatares=Avatar.objects.filter(user=request.user.id)

    if request.method == 'POST':

        miFormulario = EntrenadorFormulario(request.POST) 

        print(miFormulario)

        if miFormulario.is_valid:   

                informacion = miFormulario.cleaned_data

                entrenador = Entrenador (nombre=informacion['nombre'], apellido=informacion['apellido'],
                edad=informacion['edad'], club=informacion['club'], exjug=informacion['exjug']) 

                entrenador.save()
                
                return render(request, "AppWiki/entrenadores.html" )

    else: 

        miFormulario= EntrenadorFormulario() 
    if avatares.exists():
        return render(request, "AppWiki/agregarentrenadores.html", {"miFormulario":miFormulario,"url":avatares[0].imagen.url})
    else:
        return render(request, "AppWiki/agregarentrenadores.html", {"miFormulario":miFormulario})

def buscarEntrenador(request):
    avatares=Avatar.objects.filter(user=request.user.id)
    
    if  request.GET["apellido"]: 

        apellido = request.GET['apellido'] 
        print(apellido)
        entrenadores = Entrenador.objects.filter(apellido__icontains=apellido)
        print(entrenadores)
        if avatares.exists():
            return render(request, "AppWiki/entrenadores.html", {"entrenadores":entrenadores, "apellido":apellido,"url":avatares[0].imagen.url})
        else:
             return render(request, "AppWiki/entrenadores.html", {"entrenadores":entrenadores, "apellido":apellido})
    else:
        respuesta = "No enviaste datos"
        return render(request,"AppWiki/inicio.html", {"respuesta":respuesta})

def leerJugadores(request):
    jugadores=Jugador.objects.all()
    contexto={"jugadores":jugadores}
    return render(request,"AppWiki/leerjugadores.html", contexto)

@login_required
def eliminarJugador(request, jugador_apellido):
      jugador=Jugador.objects.get(apellido=jugador_apellido)
      jugador.delete()

      jugadores=Jugador.objects.all()
      
      contexto={"jugadores":jugadores}

      return render(request, "AppWiki/leerJugadores.html", contexto)

@login_required
def editarJugador(request, jugador_apellido):
      jugador=Jugador.objects.get(apellido= jugador_apellido)

      if request.method=="POST":
            miFormulario = JugadorFormulario(request.POST) 

            print(miFormulario)

            if miFormulario.is_valid:

                  informacion = miFormulario.cleaned_data

                  jugador.nombre=informacion['nombre']
                  jugador.apellido=informacion['apellido']
                  jugador.posicion=informacion['posicion']
                  jugador.pie=informacion['pie']
                  jugador.edad=informacion['edad']
                  jugador.club=informacion['club']
                  jugador.dorsal=informacion['dorsal']

                  jugador.save()
            return render(request, "AppWiki/leerjugadores.html")
      else:
            miFormulario=JugadorFormulario(initial={"nombre":jugador.nombre, "apellido":jugador.apellido, "posicion":jugador.posicion, "pie":jugador.pie, "edad":jugador.edad, "club":jugador.club, "dorsal":jugador.dorsal})
            return render(request, "AppWiki/editarJugadores.html", {"miFormulario":miFormulario,"jugador_apellido":jugador_apellido})

def buscarJugador(request):
    avatares=Avatar.objects.filter(user=request.user.id)
    
    if  request.GET["apellido"]: 

        apellido = request.GET['apellido'] 
        print(apellido)
        jugadores = Jugador.objects.filter(apellido__icontains=apellido)
        print(jugadores)
        if avatares.exists():
            return render(request, "AppWiki/jugadores.html", {"jugadores":jugadores, "apellido":apellido,"url":avatares[0].imagen.url})
        else:
             return render(request, "AppWiki/jugadores.html", {"jugadores":jugadores, "apellido":apellido})
    else:
        respuesta = "No enviaste datos"
        return render(request,"AppWiki/inicio.html", {"respuesta":respuesta})
    
def agregarJugador(request):
    avatares=Avatar.objects.filter(user=request.user.id)

    if request.method == 'POST':

        miFormulario = JugadorFormulario(request.POST) 

        print(miFormulario)

        if miFormulario.is_valid:   

                informacion = miFormulario.cleaned_data

                jugador = Jugador (nombre=informacion['nombre'], apellido=informacion['apellido'],
                edad=informacion['edad'], club=informacion['club'], dorsal=informacion['dorsal'], pie=informacion['pie'],posicion=informacion['posicion']) 

                jugador.save()
                
                return render(request, "AppWiki/jugadores.html" )

    else: 

        miFormulario= JugadorFormulario() 
    if avatares.exists():
        return render(request, "AppWiki/agregarjugadores.html", {"miFormulario":miFormulario,"url":avatares[0].imagen.url})
    else:
        return render(request, "AppWiki/agregarjugadores.html", {"miFormulario":miFormulario})

def buscarEquipo(request):
    avatares=Avatar.objects.filter(user=request.user.id)
    
    if  request.GET["nombre"]: 

        nombre = request.GET['nombre'] 
        print(nombre)
        equipos = Equipo.objects.filter(nombre__icontains=nombre)
        print(equipos)
        if avatares.exists():
            return render(request, "AppWiki/equipos.html", {"equipos":equipos, "nombre":nombre,"url":avatares[0].imagen.url})
        else:
             return render(request, "AppWiki/equipos.html", {"equipos":equipos, "nombre":nombre})
    else:
        respuesta = "No enviaste datos"
        return render(request,"AppWiki/inicio.html", {"respuesta":respuesta})

def sobremi(request):
    avatares=Avatar.objects.filter(user=request.user.id)
    if avatares.exists():
        return render(request, "AppWiki/sobremi.html", {"url":avatares[0].imagen.url})
    else:
        return render(request, "AppWiki/sobremi.html")


class EquipoList(LoginRequiredMixin, ListView):
    model=Equipo
    template_name="AppWiki/equipos_lista.html"

class EquipoDetalle(DetailView):
    model=Equipo
    template_name="AppWiki/equipo_detalle.html"

class EquipoCreacion(CreateView):
    model=Equipo
    success_url="/AppWiki/equipo/lista"
    fields=['nombre','liga', 'pais', 'division', 'edad', 'estadio' ]

class EquipoUpdate(UpdateView):
    model=Equipo
    success_url="/AppWiki/equipo/lista"
    fields=['nombre','liga', 'pais', 'division', 'edad', 'estadio' ]

class EquipoDelete(DeleteView):
    model=Equipo
    success_url="/AppWiki/equipo/lista"

def post(request):
    avatares=Avatar.objects.filter(user=request.user.id)
    if avatares.exists():
        return render(request, "Appwiki/post.html",{"url":avatares[0].imagen.url})
    else:
        return render(request, "Appwiki/post.html")

def post2(request):
    avatares=Avatar.objects.filter(user=request.user.id)
    if avatares.exists():
        return render(request, "Appwiki/post2.html",{"url":avatares[0].imagen.url})
    else:
        return render(request, "Appwiki/post2.html")

def post3(request):
    avatares=Avatar.objects.filter(user=request.user.id)
    if avatares.exists():
        return render(request, "Appwiki/post3.html",{"url":avatares[0].imagen.url})
    else:
        return render(request, "Appwiki/post3.html")


