from django.db import models

class Informacion_de_todos(models.Model):

    nombre=models.CharField(max_length=40)
    años = models.IntegerField()
    fecha_de_nacimiento = models.DateField()