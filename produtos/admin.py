from django.contrib import admin
from .models import *

@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = (
        'co_produto', 'co_categoria_produto', 'co_fornecedor', 'de_produto', 'nu_peso',
        'ic_controlado', 'nu_quantidade_minima'
        )

@admin.register(CategoriaProduto)
class CategoriaProdutoAdmin(admin.ModelAdmin):
    list_display = ('co_categoria_produto', 'de_categoria_produto')
