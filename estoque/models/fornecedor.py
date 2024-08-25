from django.db import models
from .cidade import Cidade

class Fornecedor(models.Model):
    ''''''

    co_fornecedor = models.AutoField(
        primary_key=True,
        unique=True,
        auto_created=True,
        editable=False
        )
    
    de_fornecedor = models.CharField(blank=False, null=False, max_length=255)
    de_endereco = models.CharField(blank=False, null=False, max_length=255)
    nu_endereco = models.IntegerField()
    de_bairro = models.CharField(blank=False, null=False, max_length=255)
    nu_cep = models.CharField(blank=False, null=False, max_length=20)
    co_cidade = models.ForeignKey(Cidade, db_column='co_cidade', on_delete=models.CASCADE)
    nu_cpf_cnpj = models.CharField(blank=False, null=False, max_length=20)
    ic_pessoa_fisica = models.IntegerField()
    no_contato = models.CharField(blank=False, null=False, max_length=255)
    nu_telefone = models.IntegerField()

    class Meta:
        db_table = 'fornecedor'
        managed = False
        app_label = 'estoque'
