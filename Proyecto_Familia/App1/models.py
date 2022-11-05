from django.db import models

class Informacion_de_todos(models.Model):

    fecha_de_nacimiento=models.IntegerField()
    lugar_de_nacimiento=models.CharField(max_length=40)
    nacionalidad=models.CharField(max_length=40)