from django.db import models

class Categoria(models.Model):
    nome = models.CharField(max_length=50)
    imagem = models.CharField(max_length=5000)

class Estabelecimento(models.Model):
    nome = models.CharField(max_length=50)
    endereco = models.CharField(max_length=500)
    usuario = models.CharField(max_length=50)
    senha = models.CharField(max_length=12)
    email = models.EmailField(max_length=254)

class Produto(models.Model):
    nome = models.CharField(max_length=300)
    descricao = models.CharField(max_length=2000)
    imagem = models.CharField(max_length=5000)
    preco = models.FloatField()
    promocao = models.IntegerField()
    Estabelecimento = models.ForeignKey(Estabelecimento, on_delete=models.CASCADE)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.nome

class Mesa(models.Model):
    estabelecimento = models.ForeignKey(Estabelecimento, on_delete=models.CASCADE)

class Consumidor(models.Model):
    nome = models.CharField(max_length=50)
    mesa = models.ForeignKey(Mesa, on_delete=models.CASCADE)
    valido_ate = models.DateTimeField(auto_now_add=True)

class Pedido(models.Model):
    consumidor = models.ForeignKey(Consumidor, on_delete=models.CASCADE)
    status = models.BooleanField()
    total = models.FloatField()

class Pedido_produto(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)