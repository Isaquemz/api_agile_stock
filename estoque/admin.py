from django.contrib import admin
from .models import *

@admin.register(Cidade)
class CidadeAdmin(admin.ModelAdmin):
    list_display = ('co_cidade', 'de_cidade', 'de_uf')

@admin.register(Fornecedor)
class FornecedorAdmin(admin.ModelAdmin):
    list_display = (
        'co_fornecedor', 'de_fornecedor', 'de_endereco', 'nu_endereco', 'de_bairro', 'nu_cep',
        'co_cidade', 'nu_cpf_cnpj', 'ic_pessoa_fisica', 'no_contato', 'nu_telefone'
        )