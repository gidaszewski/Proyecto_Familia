from django.db import models

class Familia(models.Model):

    nombre=models.CharField(max_length=40)
    años = models.IntegerField()
    fecha_de_nacimiento = models.DateField()