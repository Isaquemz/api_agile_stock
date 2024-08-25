from rest_framework import permissions
from .models import PerfilFuncionalidadeAcao

class PerfilPermissionMixin:

    def has_permission(self, co_perfil, co_funcionalidade, co_acao):
        
        try:
            acoes_permitidas = PerfilFuncionalidadeAcao.objects.filter (
                co_perfil = co_perfil,
                co_funcionalidade = co_funcionalidade,
                co_acao = co_acao,
                ic_ativo = 1
                )
            if len(acoes_permitidas) >= 1:
                return True
            else:
                return False
        except PerfilFuncionalidadeAcao.DoesNotExist:
            return False