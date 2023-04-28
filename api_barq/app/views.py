from rest_framework.decorators import api_view
from app.models import Produto
from app.serializers import ProdutoSerializer
from rest_framework.response import Response

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