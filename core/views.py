from core.models import Propiedad
from django.shortcuts import render_to_response

def lista_propiedades(request):
	propiedades = Propiedad.objects.all()
	return render_to_response('lista_propiedades.html',{'lista':propiedades})