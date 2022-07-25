from django.contrib import admin

from AppWiki.models import Entrenador, Equipo, Jugador

# Register your models here.
admin.site.register(Equipo)
admin.site.register(Entrenador)
admin.site.register(Jugador)