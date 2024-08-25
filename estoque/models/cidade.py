from django.db import models

class Cidade(models.Model):
    ''''''

    co_cidade = models.AutoField(
        primary_key=True,
        unique=True,
        auto_created=True,
        editable=False
        )
    
    de_cidade = models.CharField(blank=False, null=False, max_length=255)
    de_uf = models.CharField(blank=False, null=False, max_length=255)

    class Meta:
        db_table = 'cidade'
        managed = False
        app_label = 'estoque'
