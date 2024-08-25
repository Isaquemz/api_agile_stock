from django.db import models

class Funcionalidade(models.Model):

    co_funcionalidade = models.AutoField(
        primary_key=True,
        unique=True,
        auto_created=True,
        editable=False
        )
    
    de_funcionalidade = models.CharField(max_length=255)
    ic_ativo = models.IntegerField()

    class Meta:
        db_table = 'funcionalidade'
        managed = False
        app_label = 'auth_ag'
