#encoding:utf-8
from django.db import models
from django.contrib.auth.models import User

class Tipo_Propiedad(models.Model):
	nombre = models.CharField(max_length=30)

	def __unicode__(self):
		return self.nombre

class Propiedad(models.Model):
	nombre = models.CharField(max_length=50)
	propietario = models.ForeignKey(User)
	tipo = models.ForeignKey(Tipo_Propiedad)
	calle = models.CharField(max_length=25)
	altura = models.IntegerField()
	barrio = models.CharField(max_length=25)

	def __unicode__(self):
		return self.calle

class Propiedad_Slot(models.Model):
	propiedad = models.ForeignKey(Propiedad)
	cantidad_personas = models.IntegerField()
	esta_activo = models.BooleanField()

	def __unicode__(self):
		return self.propiedad

