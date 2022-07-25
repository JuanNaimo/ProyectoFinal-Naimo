from django.shortcuts import render
from AppCuentas.forms import UserEditForm, UserRegisterForm, AvatarFormulario
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Avatar

def login_request(request):
      
      if request.method =="POST":
            form=AuthenticationForm(request, data=request.POST)

            if form.is_valid():

                  usuario=form.cleaned_data.get('username')
                  contra=form.cleaned_data.get('password')

                  user=authenticate(username=usuario, password=contra)

                  if user is not None:
                        login(request, user)

                        return render(request, "AppWiki/inicio.html")
                  else:
                        return render(request, "AppWiki/inicio.html", {"mensaje": "Error, datos incorrectos"})
            else:
                        return render(request, "AppWiki/inicio.html", {"mensaje": "Error, formulario erroneo"})
      
      form=AuthenticationForm()

      return render(request, "AppCuentas/login.html", {"form": form})
      
def register(request):
      if request.method=="POST":

            form= UserRegisterForm(request.POST)

            if form.is_valid():
            
                  username= form.cleaned_data['username']
                  form.save()

                  return render(request, "AppWiki/inicio.html", {"mensaje":"Usuario creado"})
      else:
            form=UserRegisterForm()
      return render(request, "AppCuentas/registro.html", {"form":form})

@login_required
def editarPerfil(request):

      avatares=Avatar.objects.filter(user=request.user.id)
      usuario=request.user
      if request.method=='POST':
            
            miFormulario=UserEditForm(request.POST)
            if miFormulario.is_valid():
                  informacion=miFormulario.cleaned_data

                  usuario.email=informacion['email']
                  usuario.password1=informacion['password1']
                  usuario.password2=informacion['password2']
                  usuario.save()

                  return render(request, 'AppWiki/inicio.html')
      else:
            miFormulario=UserEditForm(initial={'email':usuario.email})
      if avatares.exists():
            return render(request, 'AppCuentas/editarPerfil.html', {"miFormulario":miFormulario, "usuario":usuario, "url":avatares[0].imagen.url})
      else:
            return render(request, 'AppCuentas/editarPerfil.html', {"miFormulario":miFormulario})

@login_required
def agregarAvatar(request):
      if request.method=="POST":
            miFormulario=AvatarFormulario(request.POST, request.FILES)

            if miFormulario.is_valid():

                  u= User.objects.get(username=request.user)
                  
                  avatar = Avatar(user=u, imagen=miFormulario.cleaned_data['imagen'])

                  avatar.save()

                  return render(request,"AppWiki/inicio.html")
      else:
            miFormulario=AvatarFormulario()
      return render(request, "AppCuentas/agregarAvatar.html", {"miFormulario":miFormulario})

