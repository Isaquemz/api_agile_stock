from django.db import models
from .cidade import Cidade

class Transportadora(models.Model):
    ''''''

    co_transportadora = models.AutoField(
        primary_key=True,
        unique=True,
        auto_created=True,
        editable=False
        )
    
    co_cidade = models.ForeignKey(Cidade, db_column='co_cidade', on_delete=models.CASCADE)
    de_transportadora = models.CharField(blank=False, null=False, max_length=255)
    nu_endereco = models.IntegerField()
    de_bairro = models.CharField(blank=False, null=False, max_length=255)
    nu_cep = models.CharField(blank=False, null=False, max_length=255)
    nu_cpf_cnpj = models.CharField(blank=False, null=False, max_length=255)
    no_contato = models.CharField(blank=False, null=False, max_length=255)
    nu_telefone = models.IntegerField()

    class Meta:
        db_table = 'transportadora'
        managed = False
        app_label = 'estoque'
