# Framework REST
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

# Usuario
from auth_ag.models import Usuario
from auth_ag.serializers import UsuarioSerializer
from .criptografia import criptografar_dados, descriptografar_dados

# Mixin
from auth_ag.permissions import PerfilPermissionMixin
from auth_ag.decorators import authenticate_token


# Views
class UsuarioAPIView(APIView):

    def __init__(self):

        # Funcionalidade da Classe
        self.co_funcionalidade = 15
        super().__init__()
    
    @authenticate_token
    def has_permission(self, request, co_acao):
        co_perfil = request.user.co_perfil
        return PerfilPermissionMixin().has_permission(co_perfil, self.co_funcionalidade, co_acao)

    def get(self, request, pk=None):

        # Ação de Leitura
        co_acao = 1

        if self.has_permission(request, co_acao):
            if pk is None:
                usuarios = Usuario.objects.all()
                serializer = UsuarioSerializer(usuarios, many=True)
            else:
                try:
                    usuario = Usuario.objects.get(pk=pk)
                except Usuario.DoesNotExist:
                    return Response(status=status.HTTP_404_NOT_FOUND)
                serializer = UsuarioSerializer(usuario)

            for data in serializer.data:
                if 'de_senha' in data:
                    senha = data['de_senha']
                    senha_criptografada = descriptografar_dados(senha)
                    data['de_senha'] = senha_criptografada

            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({'detail': 'Não autorizado.'}, status=status.HTTP_403_FORBIDDEN)
    
    def post(self, request, pk=None):

        # Ação de Criação
        co_acao = 2

        if self.has_permission(request, co_acao):
            serializer = UsuarioSerializer(data=request.data)
        else:
            return Response({'detail': 'Não autorizado.'}, status=status.HTTP_403_FORBIDDEN)

        if serializer.is_valid():

            if 'de_senha' in serializer.validated_data:
                nova_senha = serializer.validated_data['de_senha']
                senha_criptografada = criptografar_dados(nova_senha)
                serializer.validated_data['de_senha'] = senha_criptografada

            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):

        # Ação de Alteração
        co_acao = 3

        if self.has_permission(request, co_acao):
            try:
                usuario = Usuario.objects.get(pk=pk)
            except Usuario.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)
            serializer = UsuarioSerializer(usuario, data=request.data, partial=True)
        else:
            return Response({'detail': 'Não autorizado.'}, status=status.HTTP_403_FORBIDDEN)

        if serializer.is_valid():

            if 'de_senha' in serializer.validated_data:
                nova_senha = serializer.validated_data['de_senha']
                senha_criptografada = criptografar_dados(nova_senha)
                serializer.validated_data['de_senha'] = senha_criptografada

            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk=None):
        
        # Ação de Excluir
        co_acao = 4

        if self.has_permission(request, co_acao):

            try:
                usuario = Usuario.objects.get(pk=pk)
            except Usuario.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)
            
            if 'ic_desativar' in request.data and request.data.get('ic_desativar') == '1': 
                usuario.ic_ativo = 0
                usuario.save()
            else:
                usuario.delete()

            return Response(status=status.HTTP_204_NO_CONTENT)
        
        else:
            return Response({'detail': 'Não autorizado.'}, status=status.HTTP_403_FORBIDDEN)
