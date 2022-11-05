from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from AppFamiliares.models import familiar
import datetime

# Create your views here.

def vista_familiares(request):
    familiares = familiar.objects.all()
    lista_familiares = []
    for miembro in familiares:
        lista_familiares.append((miembro.nombre, miembro.apellido, miembro.fecha_nacimiento, miembro.edad))
    datos = {"listado_familiares": lista_familiares}
    plantilla = loader.get_template("listado_familiares.html")
    documento = plantilla.render(datos)
    return HttpResponse(documento)

    #cadena_respuesta = ""
    #for miembro in familiares:
    #    cadena_respuesta += f"({miembro.nombre},{miembro.apellido},{miembro.fecha_nacimiento}, {miembro.edad})" + " | "
    #return HttpResponse(cadena_respuesta)

