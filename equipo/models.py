from django.db import models

# Create your models here.

class equipo(models.Model):
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField(max_length=200)
    posicion = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
