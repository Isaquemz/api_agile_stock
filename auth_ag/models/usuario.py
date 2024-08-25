from django.db import models
from .perfil import Perfil

class Usuario(models.Model):

    co_usuario = models.AutoField(
        primary_key=True,
        unique=True,
        auto_created=True,
        editable=False
        )
    
    de_nome = models.CharField(max_length=500)
    de_nome_usuario = models.CharField(max_length=255)
    de_cpf = models.CharField(max_length=20)
    de_senha = models.CharField(max_length=255)
    de_email = models.CharField(max_length=255)
    co_perfil = models.ForeignKey(Perfil, db_column='co_perfil', on_delete=models.CASCADE)
    ic_ativo = models.IntegerField()
    dh_criacao = models.DateTimeField(auto_now_add=True)
    dh_alteracao = models.DateTimeField(auto_now=True)
    dh_ultimo_login = models.DateTimeField(null=True, blank=True)

    class Meta:
        db_table = 'usuario'
        managed = False
        app_label = 'auth_ag'
