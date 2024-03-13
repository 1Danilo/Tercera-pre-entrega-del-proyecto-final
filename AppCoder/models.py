from django.db import models


# Create your models here.

class Producto(models.Model):
    nombre = models.CharField(max_length=60)
    serie = models.CharField(max_length=255)


class Cliente(models.Model):

    nombre = models.CharField(max_length=60)
    apellido = models.CharField(max_length=60)
    correo = models.EmailField()


class Superadmin(models.Model):

    nombre = models.CharField(max_length=60)
    apellido = models.CharField(max_length=60)
    correo = models.EmailField()


class Entregable(models.Model):

    nombre = models.CharField(max_length=60)
    fechaEntrega = models.DateField()
