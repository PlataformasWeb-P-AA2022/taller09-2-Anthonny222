from django.db import models

# Create your models here.


class Equipo(models.Model):
    nombre = models.CharField(max_length=30)
    siglas = models.CharField(max_length=30)
    twitter = models.CharField(max_length=30)

    def __str__(self):
        return "%s | %s | %s" % (self.nombre,
                                 self.siglas,
                                 self.twitter)


class Jugador(models.Model):
    nombre = models.CharField(max_length=30)
    posicion = models.CharField(max_length=30)
    numero = models.IntegerField("numero de jugador")
    sueldo = models.IntegerField("sueldo de jugador")
    equipo = models.ForeignKey(
        Equipo, related_name='equipo', on_delete=models.CASCADE)

    def __str__(self):
        return "%s | %s | numero: %d | sueldo: %d - %s" % (self.nombre,
                                                           self.posicion,
                                                           self.numero,
                                                           self.sueldo,
                                                           self.equipo.nombre)


class Campeonato(models.Model):
    nombre = models.CharField(max_length=30)
    auspiciante = models.CharField(max_length=30)

    def __str__(self):
        return "%s | %s" % (self.nombre,
                            self.auspiciante)


class Equipos(models.Model):
    año = models.IntegerField("Año")
    equipo = models.CharField(max_length=30)
    campeonato = models.ForeignKey(
        Campeonato, related_name='campeonato', on_delete=models.CASCADE)

    def __str__(self):
        return "año: %d | %s | %s" % (self.año,
                                      self.equipo,
                                      self.campeonato.nombre)
