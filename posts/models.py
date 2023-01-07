from django.db import models

# Create your models here.

"""Creamos un nuevo modelo de Base de Datos llamado Posts, con la tabla text que contiene un TextField"""


class Posts(models.Model):
    text = models.TextField()

    def __str__(self):
        return self.text[:50]  # muestra los primeros 50 caracteres del TextField.
