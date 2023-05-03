from django.db import models

class Produto(models.Model):
    nome = models.CharField(max_length=300)
    descricao = models.CharField(max_length=2000)
    imagem = models.CharField(max_length=5000, null=True)
    preco = models.FloatField()
    promocao = models.IntegerField()

    def __str__(self) -> str:
        return self.nome

