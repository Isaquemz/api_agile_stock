# Framework REST
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

# Menus e Submenus
from auth_ag.models import Menu, Submenu, MenuSubmenuFuncionalidade
from auth_ag.serializers import MenuSerializer, SubmenuSerializer, MenuSubmenuFuncionalidadeSerializer

# Mixin
from auth_ag.permissions import PerfilPermissionMixin
from auth_ag.decorators import authenticate_token


# Views
class MenuAPIView(APIView):

    def __init__(self):

        # Funcionalidade da Classe
        self.co_funcionalidade = 16
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
                menus = Menu.objects.all()
                serializer = MenuSerializer(menus, many=True)
            else:
                try:
                    menu = Menu.objects.get(pk=pk)
                except Menu.DoesNotExist:
                    return Response(status=status.HTTP_404_NOT_FOUND)
                serializer = MenuSerializer(menu)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({'detail': 'Não autorizado.'}, status=status.HTTP_403_FORBIDDEN)
    
    def post(self, request, pk=None):

        # Ação de Criação
        co_acao = 2

        if self.has_permission(request, co_acao):
            serializer = MenuSerializer(data=request.data)
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
                menu = Menu.objects.get(pk=pk)
            except Menu.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)
            serializer = MenuSerializer(menu, data=request.data, partial=True)
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
                menu = Menu.objects.get(pk=pk)
            except Menu.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)
            
            if 'ic_desativar' in request.data and request.data.get('ic_desativar') == '1': 
                menu.ic_ativo = 0
                menu.save()
            else:
                menu.delete()

            return Response(status=status.HTTP_204_NO_CONTENT)
        
        else:
            return Response({'detail': 'Não autorizado.'}, status=status.HTTP_403_FORBIDDEN)


class SubmenuAPIView(APIView):

    def __init__(self):

        # Funcionalidade da Classe
        self.co_funcionalidade = 17
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
                submenus = Submenu.objects.all()
                serializer = SubmenuSerializer(submenus, many=True)
            else:
                try:
                    submenu = Submenu.objects.get(pk=pk)
                except Submenu.DoesNotExist:
                    return Response(status=status.HTTP_404_NOT_FOUND)
                serializer = SubmenuSerializer(submenu)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({'detail': 'Não autorizado.'}, status=status.HTTP_403_FORBIDDEN)
    
    def post(self, request, pk=None):

        # Ação de Criação
        co_acao = 2

        if self.has_permission(request, co_acao):
            serializer = SubmenuSerializer(data=request.data)
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
                submenu = Submenu.objects.get(pk=pk)
            except Submenu.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)
            serializer = SubmenuSerializer(submenu, data=request.data, partial=True)
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
                submenu = Submenu.objects.get(pk=pk)
            except Submenu.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)
            
            if 'ic_desativar' in request.data and request.data.get('ic_desativar') == '1':
                submenu.ic_ativo = 0
                submenu.save()
            else:
                submenu.delete()

            return Response(status=status.HTTP_204_NO_CONTENT)
        
        else:
            return Response({'detail': 'Não autorizado.'}, status=status.HTTP_403_FORBIDDEN)


class MenuSubmenuFuncionalidadeAPIView(APIView):

    def __init__(self):

        # Funcionalidade da Classe
        self.co_funcionalidade = 18
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
                menu_sub_func = MenuSubmenuFuncionalidade.objects.all()
                serializer = MenuSubmenuFuncionalidadeSerializer(menu_sub_func, many=True)
            else:
                try:
                    menu_sub_func = MenuSubmenuFuncionalidade.objects.get(pk=pk)
                except MenuSubmenuFuncionalidade.DoesNotExist:
                    return Response(status=status.HTTP_404_NOT_FOUND)
                serializer = MenuSubmenuFuncionalidadeSerializer(menu_sub_func)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({'detail': 'Não autorizado.'}, status=status.HTTP_403_FORBIDDEN)
    
    def post(self, request, pk=None):

        # Ação de Criação
        co_acao = 2

        if self.has_permission(request, co_acao):
            serializer = MenuSubmenuFuncionalidadeSerializer(data=request.data)
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
                menu_sub_func = MenuSubmenuFuncionalidade.objects.get(pk=pk)
            except MenuSubmenuFuncionalidade.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)
            serializer = MenuSubmenuFuncionalidadeSerializer(menu_sub_func, data=request.data, partial=True)
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
                menu_sub_func = MenuSubmenuFuncionalidade.objects.get(pk=pk)
            except MenuSubmenuFuncionalidade.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)
            menu_sub_func.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            return Response({'detail': 'Não autorizado.'}, status=status.HTTP_403_FORBIDDEN)
