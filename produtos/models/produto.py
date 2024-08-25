from django.db import models
from estoque.models.fornecedor import Fornecedor
from .categoria_produto import CategoriaProduto

class Produto(models.Model):
    ''''''

    co_produto = models.AutoField(
        primary_key=True,
        unique=True,
        auto_created=True,
        editable=False
        )
    
    co_categoria_produto = models.ForeignKey(CategoriaProduto, db_column='co_categoria_produto', on_delete=models.CASCADE)
    co_fornecedor = models.ForeignKey(Fornecedor, db_column='co_fornecedor', on_delete=models.CASCADE)
    de_produto = models.CharField(blank=False, null=False, max_length=255)
    nu_peso = models.DecimalField(decimal_places=2, max_digits=10)
    ic_controlado = models.IntegerField()
    nu_quantidade_minima = models.IntegerField()

    class Meta:
        db_table = 'produto'
        managed = False
        app_label = 'produtos'
