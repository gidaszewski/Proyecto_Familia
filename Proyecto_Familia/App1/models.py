from django.db import models

class Madre(models.Model):

    fecha_de_nacimiento=models.IntegerField()
    lugar_de_nacimiento=models.CharField(max_length=40)
    nacionalidad=models.CharField(max_length=40)

class Padre(models.Model):

    fecha_de_nacimiento=models.IntegerField()
    lugar_de_nacimiento=models.CharField(max_length=40)
    nacionalidad=models.CharField(max_length=40)

class Hermana(models.Model):

    fecha_de_nacimiento=models.IntegerField()
    lugar_de_nacimiento=models.CharField(max_length=40)
    nacionalidad=models.CharField(max_length=40)