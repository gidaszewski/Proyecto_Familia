from django.shortcuts import render
from django.http import HttpResponse
from django.template import Template
from django.template import loader
from App1.models import Informacion_de_todos

def Datos(request):

    info = Informacion_de_todos.objects.all()

    plantilla = loader.get_template("Template1.html")

    documento = plantilla.render(datos)

    return HttpResponse(documento)
