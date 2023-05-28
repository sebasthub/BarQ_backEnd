from rest_framework.decorators import api_view
from app.models import Produto,Categoria,Estabelecimento,Mesa,Consumidor,Pedido
from app.serializers import ProdutoSerializer,CategoriaSerializer,EstabelecimentoSerializer,MesaSerializer,ConsumidorSerializer,PedidoSerializer
from rest_framework.response import Response
from rest_framework import generics

@api_view(['GET'])
def produtos_list(request):
    produtos = Produto.objects.all()
    serializer = ProdutoSerializer(produtos,many = True)
    return Response(serializer.data)

@api_view(['GET'])
def produtos_get_by_id(request,pk):
    produtos = Produto.objects.get(id = pk)
    serializer = ProdutoSerializer(produtos,many = False)
    return Response(serializer.data)

@api_view(['GET'])
def categorias_list(request):
    categorias = Categoria.objects.all()
    serializer = CategoriaSerializer(categorias,many = True)
    return Response(serializer.data)

@api_view(['GET'])
def categorias_get_by_id(request,pk):
    categorias = Categoria.objects.get(id = pk)
    serializer = CategoriaSerializer(categorias,many = False)
    return Response(serializer.data)

class EstabelecimentoList(generics.ListCreateAPIView):
    queryset = Estabelecimento.objects.all()
    serializer_class = EstabelecimentoSerializer

class MesaList(generics.ListCreateAPIView):
    queryset = Mesa.objects.all()
    serializer_class = MesaSerializer

    @api_view(['GET'])
    def get_by_id(request,pk):
        mesa = Mesa.objects.get(id = pk)
        serializer = MesaSerializer(mesa, many = False)
        return Response(serializer.data)

class ConsumidorList(generics.ListCreateAPIView):
    queryset = Consumidor.objects.all()
    serializer_class = ConsumidorSerializer

    @api_view(['GET'])
    def get_by_id(request,pk):
        consumidor = Consumidor.objects.get(id = pk)
        serializer = ConsumidorSerializer(consumidor, many = False)
        return Response(serializer.data)

class PedidoList(generics.ListCreateAPIView):
    queryset = Pedido.objects.all()
    serializer_class = PedidoSerializer

    @api_view(['GET'])
    def get_by_id(request,pk):
        pedido = Pedido.objects.get(id = pk)
        serializer = PedidoSerializer(pedido, many = False)
        return Response(serializer.data)