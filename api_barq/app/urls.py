from django.urls import path
from app.views import ProdutoList,categorias_get_by_id,categorias_list,EstabelecimentoList,MesaList,ConsumidorList,PedidoList

urlpatterns = [
    path('produtos/', ProdutoList.as_view(), name='produtos'),
    path('produtos/<int:pk>/', ProdutoList.get_by_id),
    path('categoria/', categorias_list, name='categoria'),
    path('categoria/<int:pk>/', categorias_get_by_id),
    path('estabelecimento/', EstabelecimentoList.as_view() , name='estabelecimento'),
    path('estabelecimento/<int:pk>/', EstabelecimentoList.get_by_id , name='estabelecimento'),
    path('mesa/', MesaList.as_view(), name='mesa'),
    path('mesa/<int:pk>/', MesaList.get_by_id),
    path('consumidor/', ConsumidorList.as_view(), name='consumidor'),
    path('consumidor/<int:pk>/', ConsumidorList.get_by_id),
    path('pedido/', PedidoList.as_view(), name='pedido'),
]