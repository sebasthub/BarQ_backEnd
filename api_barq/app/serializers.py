from app.models import Produto,Categoria,Estabelecimento,Mesa,Consumidor,Pedido
from rest_framework import serializers

class ProdutoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produto
        fields =  '__all__'


class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields =  '__all__'


class EstabelecimentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estabelecimento
        fields =  '__all__'

class MesaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mesa
        fields =  '__all__'

class ConsumidorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Consumidor
        fields =  '__all__'

class PedidoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pedido
        fields =  '__all__'