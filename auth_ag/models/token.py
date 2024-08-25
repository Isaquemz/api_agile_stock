from django.db import models

from .usuario import Usuario
from .perfil import Perfil

class Token(models.Model):

    co_token = models.AutoField(
        primary_key=True,
        unique=True,
        auto_created=True,
        editable=False
        )

    co_usuario = models.ForeignKey(Usuario, db_column='co_usuario', on_delete=models.CASCADE)
    co_perfil = models.ForeignKey(Perfil, db_column='co_perfil', on_delete=models.CASCADE)
    dh_expiracao = models.DateTimeField()
    de_token = models.TextField()

    class Meta:
        db_table = 'token'
        managed = False
        app_label = 'auth'
