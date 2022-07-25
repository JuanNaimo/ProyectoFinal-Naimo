from django.urls import path
from AppWiki import views

urlpatterns = [

path('', views.inicio, name="Inicio"),
path('sobremi', views.sobremi, name="Sobremi"),
path('entrenadores', views.entrenadores, name="Entrenadores"),
path('jugadores', views.jugadores, name="Jugadores"),
path('equipos', views.equipos, name="Equipos"),
path('agregarentrenador', views.agregarentrenadores, name="AgregarEntrenador"),
path('buscarEntrenador/',views.buscarEntrenador),
path('leerjugadores', views.leerJugadores, name="LeerJugadores"),
path('eliminarJugador/<jugador_apellido>', views.eliminarJugador,name="eliminarJugador"),
path('editarJugador/<jugador_apellido>', views.editarJugador,name="editarJugador"),
path('buscarJugador/', views.buscarJugador),
path('buscarEquipo/', views.buscarEquipo),
path('agregarjugador', views.agregarJugador, name="AgregarJugador"),
path('equipo/lista',views.EquipoList.as_view(), name="List"),
path(r'^(?P<pk>\d+)$', views.EquipoDetalle.as_view(), name="Detail"),
path(r'^nuevo$', views.EquipoCreacion.as_view(), name="New"),
path(r'^editar/(?P<pk>\d+)$', views.EquipoUpdate.as_view(), name="Edit"),
path(r'^borrar/(?P<pk>\d+)$', views.EquipoDelete.as_view(), name="Delete"),
path('posteo',views.post, name="Posteo")

]



