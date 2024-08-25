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
    # Produto
    path('', ProdutoAPIView.as_view(), name='produtos'),
    path('<int:pk>/', ProdutoAPIView.as_view(), name='produtos'),

    # Categoria Produto
    path('categoria_produto/', CategoriaProdutoAPIView.as_view(), name='categoria_produto'),
    path('categoria_produto/<int:pk>/', CategoriaProdutoAPIView.as_view(), name='categoria_produto'),
]
