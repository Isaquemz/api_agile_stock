# Framework REST
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

# Model e Serialize
from produtos.models import Produto
from produtos.serializers import ProdutoSerializer

# Mixin
from auth_ag.permissions import PerfilPermissionMixin
from auth_ag.decorators import authenticate_token


# Views
class ProdutoAPIView(APIView):
    
    def __init__(self):

        # Funcionalidade da Classe
        self.co_funcionalidade = 1
        super().__init__()
    
    @authenticate_token
    def has_permission(self, request, co_acao):
        co_perfil = request.user.co_perfil
        return PerfilPermissionMixin().has_permission(co_perfil, self.co_funcionalidade, co_acao)

    def get(self, request, pk=None):
        '''
            Metodo de busca dos Produtos, sendo possivel escolher entre enviar um pk para filtro,
            ou não passar o parametro e receber todos os produtos como retorno.\n\n

            Será retornado os campos:
                "co_produto = Codigo do produto / Integer"\n
                "co_categoria_produto = Codigo da categoria do produto / Integer"\n
                "co_fornecedor = Codigo do fornecedor / Integer"\n
                "de_produto = Nome do produto / Varchar(255)"\n
                "nu_peso = Peso do produto / Integer"\n
                "ic_controlado = Indicador de produto controlado ( 1 Para sim e 0 Para não) / Integer"\n
                "nu_quantidade_minima = Quantidade minima a fim de alerta / Integer"
        '''

        # Ação de Leitura
        co_acao = 1

        has_acesso = self.has_permission(request, co_acao)
        if not isinstance(has_acesso, JsonResponse) and has_acesso:
            if pk is None:
                produtos = Produto.objects.all()
                serializer = ProdutoSerializer(produtos, many=True)
            else:
                try:
                    produto = Produto.objects.get(pk=pk)
                except Produto.DoesNotExist:
                    return Response(status=status.HTTP_404_NOT_FOUND)
                serializer = ProdutoSerializer(produto)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({'detail': 'Não autorizado.'}, status=status.HTTP_403_FORBIDDEN)

    def post(self, request, pk=None):

        # Ação de Criação
        co_acao = 2

        has_acesso = self.has_permission(request, co_acao)
        if not isinstance(has_acesso, JsonResponse) and has_acesso:
            serializer = ProdutoSerializer(data=request.data)
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
                produto = Produto.objects.get(pk=pk)
            except Produto.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)
            serializer = ProdutoSerializer(produto, data=request.data, partial=True)
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
                produto = Produto.objects.get(pk=pk)
            except Produto.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)
            produto.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            return Response({'detail': 'Não autorizado.'}, status=status.HTTP_403_FORBIDDEN)
