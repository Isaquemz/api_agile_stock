from django.db import models
from .funcionalidade import Funcionalidade

class Menu(models.Model):

    co_menu = models.AutoField(
        primary_key=True,
        unique=True,
        auto_created=True,
        editable=False
        )
    
    de_menu = models.CharField(max_length=255)
    ic_submenu = models.IntegerField()
    de_link = models.CharField(max_length=255, null=True, blank=True)
    de_icone = models.CharField(max_length=255)
    ic_ativo = models.IntegerField()

    class Meta:
        db_table = 'menu'
        managed = False
        app_label = 'auth_ag'

class Submenu(models.Model):

    co_submenu = models.AutoField(
        primary_key=True,
        unique=True,
        auto_created=True,
        editable=False
        )
    
    de_submenu = models.CharField(max_length=255)
    co_menu = models.ForeignKey(Menu, db_column='co_menu', on_delete=models.CASCADE)
    de_link = models.CharField(max_length=255)
    de_icone = models.CharField(max_length=255)
    ic_ativo = models.IntegerField()

    class Meta:
        db_table = 'submenu'
        managed = False
        app_label = 'auth_ag'

class MenuSubmenuFuncionalidade(models.Model):

    co_menu_submenu_funcionalidade = models.AutoField (
        primary_key=True,
        unique=True,
        auto_created=True,
        editable=False
        )
    
    co_submenu = models.ForeignKey(Submenu, db_column='co_submenu', on_delete=models.CASCADE, null=True, blank=True)
    co_menu = models.ForeignKey(Menu, db_column='co_menu', on_delete=models.CASCADE)
    co_funcionalidade = models.ForeignKey(Funcionalidade, db_column='co_funcionalidade', on_delete=models.CASCADE)
   
    class Meta:
        db_table = 'menu_submenu_funcionalidade'
        managed = False
        app_label = 'auth_ag'
