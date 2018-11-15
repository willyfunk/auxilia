from django.db import models

# Create your models here.


class Persona(models.Model):

    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    correo = models.CharField(max_length=30)
    telefono = models.CharField(max_length=15)
    asunto = models.CharField(max_length=50)
    mensaje = models.CharField(max_length=150)
    estado = models.CharField(max_length=20)
    respuesta = models.CharField(max_length=150)