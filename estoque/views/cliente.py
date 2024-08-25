from django.shortcuts import render

# Framework REST
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

# Cliente
from estoque.models import Cliente
from estoque.serializers import ClienteSerializer


# Mixin
from auth_ag.permissions import PerfilPermissionMixin
from auth_ag.decorators import authenticate_token


# Views
class ClienteAPIView(APIView):

    def __init__(self):

        # Funcionalidade da Classe
        self.co_funcionalidade = 6
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
                clientes = Cliente.objects.all()
                serializer = ClienteSerializer(clientes, many=True)
            else:
                try:
                    cliente = Cliente.objects.get(pk=pk)
                except Cliente.DoesNotExist:
                    return Response(status=status.HTTP_404_NOT_FOUND)
                serializer = ClienteSerializer(cliente)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({'detail': 'Não autorizado.'}, status=status.HTTP_403_FORBIDDEN)
    
    def post(self, request, pk=None):

        # Ação de Criação
        co_acao = 2

        if self.has_permission(request, co_acao):
            serializer = ClienteSerializer(data=request.data)
        else:
            return Response({'detail': 'Não autorizado.'}, status=status.HTTP_403_FORBIDDEN)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):

        # Ação de Alteração
        co_acao = 3

        if self.has_permission(request, co_acao):
            try:
                cliente = Cliente.objects.get(pk=pk)
            except Cliente.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)
            serializer = ClienteSerializer(cliente, data=request.data, partial=True)
        else:
            return Response({'detail': 'Não autorizado.'}, status=status.HTTP_403_FORBIDDEN)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk=None):

        # Ação de Excluir
        co_acao = 4

        if self.has_permission(request, co_acao):

            try:
                cliente = Cliente.objects.get(pk=pk)
            except Cliente.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)
            
            cliente.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        
        else:
            return Response({'detail': 'Não autorizado.'}, status=status.HTTP_403_FORBIDDEN)
