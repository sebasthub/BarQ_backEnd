from django.contrib import admin
from app.models import Produto,Estabelecimento,Categoria,Mesa,Consumidor,Pedido,Pedido_produto

# Register your models here.
admin.site.register(Produto)
admin.site.register(Estabelecimento)
admin.site.register(Categoria)
admin.site.register(Mesa)
admin.site.register(Consumidor)
admin.site.register(Pedido)
admin.site.register(Pedido_produto)