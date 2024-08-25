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
    # Cidade
    path('cidade/', CidadeAPIView.as_view(), name='cidade'),
    path('cidade/<int:pk>/', CidadeAPIView.as_view(), name='cidade'),

    # Fornecedor
    path('fornecedor/', FornecedorAPIView.as_view(), name='fornecedor'),
    path('fornecedor/<int:pk>/', FornecedorAPIView.as_view(), name='fornecedor'),

    # Cliente
    path('cliente/', ClienteAPIView.as_view(), name='cliente'),
    path('cliente/<int:pk>/', ClienteAPIView.as_view(), name='cliente'),

    # Transportadora
    path('transportadora/', TransportadoraAPIView.as_view(), name='transportadora'),
    path('transportadora/<int:pk>/', TransportadoraAPIView.as_view(), name='transportadora'),
]
