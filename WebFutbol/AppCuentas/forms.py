from django import forms
from dataclasses import fields
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class AvatarFormulario(forms.Form):
    imagen=forms.ImageField()

class UserRegisterForm(UserCreationForm):

    last_name: forms.CharField()
    email = forms.EmailField()
    password1 = forms.CharField(label= 'Contraseña', widget= forms.PasswordInput)
    password2 = forms.CharField(label= 'Repite la contraseña', widget=forms.PasswordInput)
    

   
    class Meta:
        model = User                                             
        fields = ['username','last_name', 'email', 'password1', 'password2']
        labels = {'username': 'Nombre', 'email':'correo','last_name': 'Apellido'}
        help_texts= {k:"" for k in fields}

class UserEditForm(UserCreationForm):

    email = forms.EmailField(label='Modificar email')
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repita contraseña', widget=forms.PasswordInput)
    
    class Meta:
        model = User
        fields = ['email', 'password1', 'password2']
        help_texts= {k:"" for k in fields}
