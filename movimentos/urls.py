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
    # Entrada
    path('entrada/', EntradaAPIView.as_view(), name='entrada'),
    path('entrada/<int:pk>/', EntradaAPIView.as_view(), name='entrada'),

    # Entrada Produto
    path('entrada_produto/', EntradaProdutoAPIView.as_view(), name='entrada_produto'),
    path('entrada_produto/<int:pk>/', EntradaProdutoAPIView.as_view(), name='entrada_produto'),

    # Saida
    path('saida/', SaidaAPIView.as_view(), name='saida'),
    path('saida/<int:pk>/', SaidaAPIView.as_view(), name='saida'),

    # Saida Produto
    path('saida_produto/', SaidaProdutoAPIView.as_view(), name='saida_produto'),
    path('saida_produto/<int:pk>/', SaidaProdutoAPIView.as_view(), name='saida_produto'),
]
