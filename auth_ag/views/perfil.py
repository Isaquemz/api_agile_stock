# Framework REST
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

# Perfil
from auth_ag.models import Perfil
from auth_ag.serializers import PerfilSerializer

# Mixin
from auth_ag.permissions import PerfilPermissionMixin
from auth_ag.decorators import authenticate_token


# Views
class PerfilAPIView(APIView):

    def __init__(self):

        # Funcionalidade da Classe
        self.co_funcionalidade = 13
        super().__init__()
    
    @authenticate_token
    def has_permission(self, request, co_acao):
        co_perfil = request.user.co_perfil
        return PerfilPermissionMixin().has_permission(co_perfil, self.co_funcionalidade, co_acao)

    def get(self, request, pk=None):
        # Ação de Leitura
        co_acao = 1

        has_acesso = self.has_permission(request, co_acao)
        if not isinstance(has_acesso, JsonResponse) and has_acesso:
            if pk is None:
                perfis = Perfil.objects.all()
                serializer = PerfilSerializer(perfis, many=True)
            else:
                try:
                    perfil = Perfil.objects.get(pk=pk)
                except Perfil.DoesNotExist:
                    return Response(status=status.HTTP_404_NOT_FOUND)
                serializer = PerfilSerializer(perfil)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({'detail': 'Não autorizado.'}, status=status.HTTP_403_FORBIDDEN)
    
    def post(self, request, pk=None):

        # Ação de Criação
        co_acao = 2

        has_acesso = self.has_permission(request, co_acao)
        if not isinstance(has_acesso, JsonResponse) and has_acesso:
            serializer = PerfilSerializer(data=request.data)
        else:
            return Response({'detail': 'Não autorizado.'}, status=status.HTTP_403_FORBIDDEN)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):

        # Ação de Alteração
        co_acao = 3

        has_acesso = self.has_permission(request, co_acao)
        if not isinstance(has_acesso, JsonResponse) and has_acesso:
            try:
                perfil = Perfil.objects.get(pk=pk)
            except Perfil.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)
            serializer = PerfilSerializer(perfil, data=request.data, partial=True)
        else:
            return Response({'detail': 'Não autorizado.'}, status=status.HTTP_403_FORBIDDEN)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk=None):

        # Ação de Excluir
        co_acao = 4

        has_acesso = self.has_permission(request, co_acao)
        if not isinstance(has_acesso, JsonResponse) and has_acesso:

            try:
                perfil = Perfil.objects.get(pk=pk)
            except Perfil.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)
            
            if 'ic_desativar' in request.data and request.data.get('ic_desativar') == '1': 
                perfil.ic_ativo = 0
                perfil.save()
            else:
                perfil.delete()

            return Response(status=status.HTTP_204_NO_CONTENT)

        else:
            return Response({'detail': 'Não autorizado.'}, status=status.HTTP_403_FORBIDDEN)
