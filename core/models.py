#encoding:utf-8
from django.db import models

# Obsoleto - Referencia al modelo de usuario antiguo
#from django.contrib.auth.models import User

# Para referenciar al nuevo modelo de usuario
from django.conf import settings




class Tipo_Propiedad(models.Model):
	nombre = models.CharField(max_length=30)

	def __unicode__(self):
		return self.nombre

class Propiedad(models.Model):
	nombre = models.CharField(max_length=50, null=True, blank=True)
	propietario = models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name="pertenece")
	tipo = models.ForeignKey(to=Tipo_Propiedad, related_name="es")
	calle = models.CharField(max_length=25)
	altura = models.IntegerField()
	barrio = models.CharField(max_length=25, null=True, blank=True)

	def __unicode__(self):
		return self.calle

class Propiedad_Slot(models.Model):
	propiedad = models.ForeignKey(to=Propiedad, related_name="pertenece")
	cantidad_personas = models.IntegerField()
	esta_activo = models.BooleanField(verbose_name='Activo', default=True, help_text='Indica si el espacio habitacional esta habitable o no.')

	def __unicode__(self):
		return unicode(self.propiedad)
