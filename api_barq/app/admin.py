from django.contrib import admin
from app.models import Produto,Estabelecimento,Categoria,Mesa,Consumidor

# Register your models here.
admin.site.register(Produto)
admin.site.register(Estabelecimento)
admin.site.register(Categoria)
admin.site.register(Mesa)
admin.site.register(Consumidor)