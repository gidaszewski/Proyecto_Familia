from django.shortcuts import render
from django.http import HttpResponse
from django.template import Template
from django.template import loader
from App1.models import Familia

def Datos(request):

    infoFamilia = Familia.objects.all()

    datos_familiares = {"infoFamilia": infoFamilia}

    plantilla = loader.get_template("Template1.html")
    
    documento =  plantilla.render(datos_familiares)
    
    return HttpResponse(documento)    
