from django.urls import path
from AppCuentas import views
from django.contrib.auth.views import LogoutView

urlpatterns=[

path('registro', views.register, name="Registro"),
path('logout', LogoutView.as_view(template_name='AppWiki/inicio.html'), name= 'Logout'),
path('login', views.login_request, name="Login"),
path('editarPerfil', views.editarPerfil, name="EditarPerfil"),
path('agregaravatar', views.agregarAvatar, name="AgregarAvatar"),
]