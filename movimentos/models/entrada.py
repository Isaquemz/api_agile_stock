from django.db import models
from estoque.models.transportadora import Transportadora

class Entrada(models.Model):

    co_entrada = models.AutoField(
        primary_key=True,
        unique=True,
        auto_created=True,
        editable=False
        )
    
    co_transportadora = models.ForeignKey(Transportadora, db_column='co_transportadora', on_delete=models.CASCADE)
    dt_pedido = models.DateField()
    dt_entrada = models.DateField()
    vr_total = models.DecimalField(decimal_places=2, max_digits=10)
    vr_frete = models.DecimalField(decimal_places=2, max_digits=10)
    vr_imposto = models.DecimalField(decimal_places=2, max_digits=10)
    nu_nota_fiscal = models.IntegerField()

    class Meta:
        db_table = 'entrada'
        managed = False
        app_label = 'movimentos'
