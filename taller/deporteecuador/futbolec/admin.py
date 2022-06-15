from django.contrib import admin

# Register your models here.
from futbolec.models import Equipo, Jugador, Campeonato, Equipos


class EquipoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'siglas', 'twitter')


admin.site.register(Equipo, EquipoAdmin)


class JugadorAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'posicion', 'numero', 'sueldo', 'equipo')


admin.site.register(Jugador, JugadorAdmin)


class CampeonatoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'auspiciante')


admin.site.register(Campeonato, CampeonatoAdmin)


class EquiposAdmin(admin.ModelAdmin):
    list_display = ('año', 'equipo', 'campeonato')


admin.site.register(Equipos, EquiposAdmin)
