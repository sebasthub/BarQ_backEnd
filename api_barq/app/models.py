from django.db import models

class Produto(models.Model):
    nome = models.CharField(max_length=300)
    descricao = models.CharField(max_length=2000)
    preco = models.FloatField()
    promocao = models.IntegerField()

