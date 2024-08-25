"""
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
"""
from django.urls import path
from .views import *

urlpatterns = [

    # Login
    path('login/', LoginAPIView.as_view(), name='login'),
    path('logout/', LogoutAPIView.as_view(), name='logout'),
    path('valid_token/', ValidTokenAPIView.as_view(), name='valid_token'),

    # Acao
    path('acao/', AcaoAPIView.as_view(), name='acao'),
    path('acao/<int:pk>/', AcaoAPIView.as_view(), name='acao'),

    # Funcionalidade
    path('funcionalidade/', FuncionalidadeAPIView.as_view(), name='funcionalidade'),
    path('funcionalidade/<int:pk>/', FuncionalidadeAPIView.as_view(), name='funcionalidade'),

    # Perfil Funcionalidade Acao
    path('perfil_funcionalidade_acao/', PerfilFuncionalidadeAcaoAPIView.as_view(), name='perfil_funcionalidade_acao'),
    path('perfil_funcionalidade_acao/<int:pk>/', PerfilFuncionalidadeAcaoAPIView.as_view(), name='perfil_funcionalidade_acao'),

    # Perfil
    path('perfil/', PerfilAPIView.as_view(), name='perfil'),
    path('perfil/<int:pk>/', PerfilAPIView.as_view(), name='perfil'),

    # Usuario
    path('usuario/', UsuarioAPIView.as_view(), name='usuario'),
    path('usuario/<int:pk>/', UsuarioAPIView.as_view(), name='usuario'),

    # Menu
    path('menu/', MenuAPIView.as_view(), name='menu'),
    path('menu/<int:pk>/', MenuAPIView.as_view(), name='menu'),

    # Submenu
    path('submenu/', SubmenuAPIView.as_view(), name='submenu'),
    path('submenu/<int:pk>/', SubmenuAPIView.as_view(), name='submenu'),
    
    # MenuSubmenuFuncionalidade
    path('menu_submenu_funcionalidade/', MenuSubmenuFuncionalidadeAPIView.as_view(), name='menu_submenu_funcionalidade'),
    path('menu_submenu_funcionalidade/<int:pk>/', MenuSubmenuFuncionalidadeAPIView.as_view(), name='menu_submenu_funcionalidade'),

]
