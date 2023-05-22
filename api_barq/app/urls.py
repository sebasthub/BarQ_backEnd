from django.urls import path
from app.views import produtos_list,produtos_get_by_id,categorias_get_by_id,categorias_list,EstabelecimentoList,MesaList,ConsumidorList,PedidoList

urlpatterns = [
    path('produtos/', produtos_list),
    path('produtos/<int:pk>/', produtos_get_by_id),
    path('categoria/', categorias_list),
    path('categoria/<int:pk>/', categorias_get_by_id),
    path('Estabelecimento/', EstabelecimentoList.as_view()),
    path('mesa/', MesaList.as_view()),
    path('consumidor/', ConsumidorList.as_view()),
    path('pedido/', PedidoList.as_view()),
]