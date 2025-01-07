from django.db import models

class Book(models.Model):
    titulo = models.CharField(max_length=255)
    ano_pub = models.IntegerField()
    autor = models.CharField(max_length=100)
    numero_paginas = models.IntegerField()
    