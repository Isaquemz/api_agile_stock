from rest_framework import serializers
from .models import *

class EntradaSerializer(serializers.ModelSerializer):

    class Meta:
        extra_kwargs = {
            'co_entrada': {'read_only': True}
        }
        model = Entrada
        fields = (
            'co_entrada',
            'co_transportadora',
            'dt_pedido',
            'dt_entrada',
            'vr_total',
            'vr_frete',
            'vr_imposto',
            'nu_nota_fiscal'
        )

class EntradaProdutoSerializer(serializers.ModelSerializer):

    class Meta:
        extra_kwargs = {
            'co_entrada_produto': {'read_only': True}
        }
        model = EntradaProduto
        fields = (
            'co_entrada_produto',
            'co_produto',
            'co_entrada',
            'nu_lote',
            'nu_quantidade',
            'vr_total'
        )

class SaidaSerializer(serializers.ModelSerializer):

    class Meta:
        extra_kwargs = {
            'co_saida': {'read_only': True}
        }
        model = Saida
        fields = (
            'co_saida',
            'co_cliente',
            'co_transportadora',
            'vr_total',
            'vr_frete',
            'vr_imposto'
        )

class SaidaProdutoSerializer(serializers.ModelSerializer):

    class Meta:
        extra_kwargs = {
            'co_saida_produto': {'read_only': True}
        }
        model = SaidaProduto
        fields = (
            'co_saida_produto',
            'co_saida',
            'co_produto',
            'nu_lote',
            'nu_quantidade',
            'vr_total'
        )
