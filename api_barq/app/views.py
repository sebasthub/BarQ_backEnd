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

class ConsumidorList(generics.ListCreateAPIView):
    queryset = Consumidor.objects.all()
    serializer_class = ConsumidorSerializer

class PedidoList(generics.ListCreateAPIView):
    queryset = Pedido.objects.all()
    serializer_class = PedidoSerializer