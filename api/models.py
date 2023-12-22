from django.db import models

class Artista(models.Model):
    nome = models.CharField(max_length=30)
    genero = models.CharField(max_length=15)
    