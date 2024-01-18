from django.db import models
from datetime import datetime
# Create your models here.
class Examen(models.Model):
    asignature = models.CharField(max_length=90)
    date = models.TextField(max_length=11)
    fecha_creacion = models.DateTimeField(default=datetime.now(), blank=True)
    def __str__(self) -> str:
        return self.asignature
class Apunte(models.Model):
    Asignatura = models.CharField(max_length=40)
    tema = models.CharField(max_length=4)
    text = models.TextField(max_length=10000)
    fecha_creacion = models.DateTimeField(default=datetime.now(), blank=True)
    def __str__(self) -> str:
        return self.Asignatura