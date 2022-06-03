from django.db import models
from django.contrib.auth.models import User

class ProcessadorIniciante(models.Model):
    correto = models.IntegerField()
    errado = models.IntegerField()
