from django.db import models

class Pesquisa(models.Model):
    titulo = models.CharField(max_length=200, default='nulo')
    preco_parcelado = models.CharField(max_length=50, default='nulo')
    preco_boleto = models.CharField(max_length=50, default='nulo')
    data_inserida = models.DateField()

    def __str__(self):
        return self.titulo