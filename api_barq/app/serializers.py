from app.models import Produto,Categoria,Estabelecimento,Mesa,Consumidor,Pedido
from rest_framework import serializers

class ProdutoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produto
        fields =  ['id','nome','descricao','preco','promocao','imagem',]


class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields =  ['id','nome',]


class EstabelecimentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estabelecimento
        fields =  ['id','endereco','usuario',"senha","email",]

class MesaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mesa
        fields =  ['id','estabelecimento',]

class ConsumidorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Consumidor
        fields =  ['id','nome','mesa','valido_ate']

class PedidoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pedido
        fields =  ['id','consumidor','status','total']