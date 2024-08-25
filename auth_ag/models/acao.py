from django.db import models

class Acao(models.Model):

    co_acao = models.AutoField(
        primary_key=True,
        unique=True,
        auto_created=True,
        editable=False
        )
    
    de_acao = models.CharField(max_length=255)
    ic_ativo = models.IntegerField()

    class Meta:
        db_table = 'acao'
        managed = False
        app_label = 'auth_ag'
