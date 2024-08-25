from django.db import models
from produtos.models.produto import Produto
from .entrada import Entrada

class EntradaProduto(models.Model):

    co_entrada_produto = models.AutoField(
        primary_key=True,
        unique=True,
        auto_created=True,
        editable=False
        )
    
    co_produto = models.ForeignKey(Produto, db_column='co_produto', on_delete=models.CASCADE)
    co_entrada = models.ForeignKey(Entrada, db_column='co_entrada', on_delete=models.CASCADE)
    nu_lote = models.IntegerField()
    nu_quantidade = models.IntegerField()
    vr_total = models.DecimalField(decimal_places=2, max_digits=10)

    class Meta:
        db_table = 'entrada_produto'
        managed = False
        app_label = 'movimentos'
