from django.db import models

# Create your models here.

class familiar(models.Model):
    nombre = models.CharField(max_length = 40)
    apellido = models.CharField(max_length = 40)
    fecha_nacimiento = models.DateField()
    edad = models.IntegerField()

    