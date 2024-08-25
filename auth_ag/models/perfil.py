from django.db import models

class Perfil(models.Model):

    co_perfil = models.AutoField(
        primary_key=True,
        unique=True,
        auto_created=True,
        editable=False
        )
    
    de_perfil = models.CharField(max_length=255)
    ic_ativo = models.IntegerField()

    class Meta:
        db_table = 'perfil'
        managed = False
        app_label = 'auth'
