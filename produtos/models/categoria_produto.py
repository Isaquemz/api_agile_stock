from django.db import models

class CategoriaProduto(models.Model):
    ''''''
    
    co_categoria_produto = models.AutoField(
        primary_key=True,
        unique=True,
        auto_created=True,
        editable=False
        )
    
    de_categoria_produto = models.CharField(blank=False, null=False, max_length=255)

    class Meta:
        db_table = 'categoria_produto'
        managed = False
        app_label = 'produtos'
