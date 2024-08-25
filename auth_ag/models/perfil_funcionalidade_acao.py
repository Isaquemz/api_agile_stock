from django.db import models
from .perfil import Perfil
from .funcionalidade import Funcionalidade
from .acao import Acao

class PerfilFuncionalidadeAcao(models.Model):

    co_perfil_funcionalidade_acao = models.AutoField(
        primary_key=True,
        unique=True,
        auto_created=True,
        editable=False
        )
    
    co_perfil = models.ForeignKey(Perfil, db_column='co_perfil', on_delete=models.CASCADE)
    co_funcionalidade = models.ForeignKey(Funcionalidade, db_column='co_funcionalidade', on_delete=models.CASCADE)
    co_acao = models.ForeignKey(Acao, db_column='co_acao', on_delete=models.CASCADE)
    ic_ativo = models.IntegerField()
    dh_criacao = models.DateTimeField(auto_now_add=True)
    dh_alteracao = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'perfil_funcionalidade_acao'
        managed = False
        app_label = 'auth_ag'
