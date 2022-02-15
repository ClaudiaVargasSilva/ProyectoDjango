from django.db import models

####################################################
# KARAOKE
####################################################
class Karaoke(models.Model):
    nombreCancion   = models.CharField(max_length=40)
    artista         = models.CharField(max_length=40)

    def __str__(self):
        return self.nombreCancion

####################################################
# PARTICIPANTES
####################################################
class Participantes(models.Model):
    nombre          = models.CharField(max_length=40)
    edad            = models.IntegerField()
    anioInscripcion = models.DateField()
    email           = models.EmailField()

    def __str__(self):
        return self.nombre

####################################################
# GANADORES
####################################################
class Ganadores(models.Model):
    nombre          = models.CharField(max_length=40)
    nombreCancion   = models.CharField(max_length=40)
    anioWin         = models.IntegerField()

    def __str__(self):
        return f'{self.nombre} {self.nombreCancion}'
