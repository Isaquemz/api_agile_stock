from rest_framework import serializers
from .models import *

class AcaoSerializer(serializers.ModelSerializer):

    class Meta:
        extra_kwargs = {
            'co_acao': {'read_only': True}
        }
        model = Acao
        fields = (
            'co_acao',
            'de_acao',
            'ic_ativo'
        )

class FuncionalidadeSerializer(serializers.ModelSerializer):

    class Meta:
        extra_kwargs = {
            'co_funcionalidade': {'read_only': True}
        }
        model = Funcionalidade
        fields = (
            'co_funcionalidade',
            'de_funcionalidade',
            'ic_ativo'
        )

class PerfilSerializer(serializers.ModelSerializer):

    class Meta:
        extra_kwargs = {
            'co_perfil': {'read_only': True}
        }
        model = Perfil
        fields = (
            'co_perfil',
            'de_perfil',
            'ic_ativo'
        )

class PerfilFuncionalidadeAcaoSerializer(serializers.ModelSerializer):

    class Meta:
        extra_kwargs = {
            'co_perfil_funcionalidade_acao': {'read_only': True}
        }
        model = PerfilFuncionalidadeAcao
        fields = (
            'co_perfil_funcionalidade_acao',
            'co_perfil',
            'co_funcionalidade',
            'co_acao',
            'ic_ativo',
            'dh_criacao',
            'dh_alteracao'
        )

class UsuarioSerializer(serializers.ModelSerializer):

    class Meta:
        extra_kwargs = {
            'co_usuario': {'read_only': True},
            'de_senha': {'write_only': True}
        }
        model = Usuario
        fields = (
            'co_usuario',
            'de_nome',
            'de_nome_usuario',
            'de_cpf',
            'de_senha',
            'de_email',
            'co_perfil',
            'ic_ativo',
            'dh_criacao',
            'dh_alteracao',
            'dh_ultimo_login'
        )

class MenuSerializer(serializers.ModelSerializer):

    class Meta:
        extra_kwargs = {
            'co_menu': {'read_only': True}
        }
        model = Menu
        fields = (
            'co_menu',
            'de_menu',
            'ic_submenu',
            'de_link',
            'de_icone',
            'ic_ativo'
        )

class SubmenuSerializer(serializers.ModelSerializer):

    class Meta:
        extra_kwargs = {
            'co_submenu': {'read_only': True}
        }
        model = Submenu
        fields = (
            'co_submenu',
            'de_submenu',
            'co_menu',
            'de_link',
            'de_icone',
            'ic_ativo'
        )

class MenuSubmenuFuncionalidadeSerializer(serializers.ModelSerializer):

    class Meta:
        extra_kwargs = {
            'co_menu_submenu_funcionalidade': {'read_only': True}
        }
        model = MenuSubmenuFuncionalidade
        fields = (
            'co_menu_submenu_funcionalidade',
            'co_submenu',
            'co_menu',
            'co_funcionalidade'
        )
