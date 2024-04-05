from django.db import models

class Ata(models.Model):
    dataInicio = models.DateField(auto_now=True)
    dataFinal = models.DateField()
    titulo = models.CharField(max_length=255)
    pauta = models.TextField()
    descricao = models.TextField('Descrição')