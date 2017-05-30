# -*- coding: utf-8 -*-

from django.db import models

class Reservas(models.Model):
    id_reserva = models.AutoField(primary_key=True)
    fecha_e = models.CharField(max_length=10)
    fecha_s = models.CharField(max_length=10)
    usuario = models.CharField(max_length=9)
    adultos = models.IntegerField(default=0)
    ninos = models.IntegerField(default=0)

    def __unicode__(self):
        return self.id_reserva

class Comentarios(models.Model):
    id_comentario = models.AutoField(primary_key=True)
    usuario = models.CharField(max_length=9)
    texto = models.TextField()

    def __unicode__(self):
        return self.texto
