from rest_framework import serializers
from .models import *

class ProdutoSerializer(serializers.ModelSerializer):

    de_categoria_produto = serializers.SerializerMethodField()
    de_fornecedor = serializers.SerializerMethodField()

    class Meta:
        extra_kwargs = {
            'co_produto': {'read_only': True},
            'de_categoria_produto': {'read_only': True},
            'de_fornecedor': {'read_only': True}
        }
        model = Produto
        fields = (
            'co_produto',
            'co_categoria_produto',
            'de_categoria_produto',
            'co_fornecedor',
            'de_fornecedor',
            'de_produto',
            'nu_peso',
            'ic_controlado',
            'nu_quantidade_minima'
        )

    def get_de_categoria_produto(self, obj):
        return obj.co_categoria_produto.de_categoria_produto
    
    def get_de_fornecedor(self, obj):
        return obj.co_fornecedor.de_fornecedor

class CategoriaProdutoSerializer(serializers.ModelSerializer):

    class Meta:
        extra_kwargs = {
            'co_categoria_produto': {'read_only': True}
        }
        model = CategoriaProduto
        fields = (
            'co_categoria_produto',
            'de_categoria_produto',
        )
