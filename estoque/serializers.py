from rest_framework import serializers
from .models import *

class CidadeSerializer(serializers.ModelSerializer):
    
    class Meta:
        extra_kwargs = {
            'co_cidade': {'read_only': True}
        }
        model = Cidade
        fields = (
            'co_cidade',
            'de_cidade',
            'de_uf'
        )

class FornecedorSerializer(serializers.ModelSerializer):

    class Meta:
        extra_kwargs = {
            'co_fornecedor': {'read_only': True}
        }
        model = Fornecedor
        fields = (
            'co_fornecedor',
            'de_fornecedor',
            'de_endereco',
            'nu_endereco',
            'de_bairro',
            'nu_cep',
            'co_cidade',
            'nu_cpf_cnpj',
            'ic_pessoa_fisica',
            'no_contato',
            'nu_telefone'
        )

class ClienteSerializer(serializers.ModelSerializer):

    class Meta:
        extra_kwargs = {
            'co_cliente': {'read_only': True}
        }
        model = Cliente
        fields = (
            'co_cliente',
            'no_cliente',
            'de_endereco',
            'nu_endereco',
            'de_bairro',
            'nu_cep',
            'co_cidade',
            'nu_cpf_cnpj',
            'ic_pessoa_fisica',
            'no_contato',
            'nu_telefone'
        )

class TransportadoraSerializer(serializers.ModelSerializer):

    class Meta:
        extra_kwargs = {
            'co_transportadora': {'read_only': True}
        }
        model = Transportadora
        fields = (
            'co_transportadora',
            'co_cidade',
            'de_transportadora',
            'nu_endereco',
            'de_bairro',
            'nu_cep',
            'nu_cpf_cnpj',
            'no_contato',
            'nu_telefone'
        )
