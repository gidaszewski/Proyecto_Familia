from django.shortcuts import render
from django.http import HttpResponse
from django.template import Template, Context
from django.template import loader
from App1.models import Informacion_de_todos

def Datos(self):

    #nombres
    nombre_madre="Lucrecia"
    nombre_padre="Guillermo"
    nombre_hermana="Bárbara"

    #apellidos
    apellido_madre="Castro"
    apellido_padre="Gidaszewski"
    apellido_hermana="Gidaszewski"

    diccionario = {"Madre": nombre_madre, "Apellidomadre": apellido_madre,
    "Padre": nombre_padre, "Apellidopadre": apellido_padre,
    "Hermana": nombre_hermana, "Apellidohermana": apellido_hermana}

    plantilla= loader.get_template('template1.html')

    documento = plantilla.render(diccionario)

    return HttpResponse(documento)

def infomadre(self):
    
    fecha=Informacion_de_todos(fecha_de_nacimiento="23/03/1969")
    lugar=Informacion_de_todos(lugar_de_nacimiento="Paraná, Entre Ríos")
    nacio=Informacion_de_todos(nacionalidad="Argentina")
    infomadre.save()
    documentoDeTexto=f"""Fecha de nacimiento: {infomadre.fecha_de_nacimiento}
    #Lugar de nacimiento: {infomadre.lugar_de_nacimiento}
    #Nacionalidad: {infomadre.nacionalidad}"""

    return HttpResponse(documentoDeTexto)
    

def infopadre(self):

    fecha=Padre(fecha_de_nacimiento="23/10/1970")
    lugar=Padre(lugar_de_nacimiento="Crespo, Entre Ríos")
    nacio=Padre(nacionalidad="Argentino")
    infopadre.save()
    documentoDeTexto=f"""Fecha de nacimiento: {infopadre.fecha_de_nacimiento}
    Lugar de nacimiento: {infopadre.lugar_de_nacimiento}
    Nacionalidad: {infopadre.nacionalidad}"""

    return HttpResponse(documentoDeTexto)

def infohermana(self):

    fecha=Hermana(fecha_de_nacimiento="20/03/2004")
    lugar=Hermana(lugar_de_nacimiento="Paraná, Entre Ríos")
    nacio=Hermana(nacionalidad="Argentina")
    infohermana.save()
    documentoDeTexto=f"""Fecha de nacimiento: {infohermana.fecha_de_nacimiento}
    Lugar de nacimiento: {infohermana.lugar_de_nacimiento}
    Nacionalidad: {infohermana.nacionalidad}"""

    return HttpResponse(documentoDeTexto)


