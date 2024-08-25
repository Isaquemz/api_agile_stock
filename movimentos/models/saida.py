from django.db import models
from estoque.models.cliente import Cliente
from estoque.models.transportadora import Transportadora

class Saida(models.Model):

    co_saida = models.AutoField(
        primary_key=True,
        unique=True,
        auto_created=True,
        editable=False
        )
    
    co_cliente = models.ForeignKey(Cliente, db_column='co_cliente', on_delete=models.CASCADE)
    co_transportadora = models.ForeignKey(Transportadora, db_column='co_transportadora', on_delete=models.CASCADE)
    vr_total = models.DecimalField(decimal_places=2, max_digits=10)
    vr_frete = models.DecimalField(decimal_places=2, max_digits=10)
    vr_imposto = models.DecimalField(decimal_places=2, max_digits=10)    

    class Meta:
        db_table = 'saida'
        managed = False
        app_label = 'movimentos'
