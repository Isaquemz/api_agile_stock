"""
URL configuration for api_agile_stock project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
import os
from django.conf import settings

readme_path = os.path.join(settings.BASE_DIR, 'README.md')
with open(readme_path, 'r', encoding='utf-8') as file:
    content = file.read()

# Configuração do schema do Swagger
schema_view = get_schema_view(
    openapi.Info(
        title="Api Agile Stock",
        default_version='v1.0.0',
        description=content,
        contact=openapi.Contact(
            name="Isaque Menezes",
            email="isaquesantos1517@gmail.com",
            url="https://www.linkedin.com/in/isaque-menezes/"
        ),
    ),
    public=True,
    permission_classes=[permissions.AllowAny,],
)

urlpatterns = [
    path('admin/', admin.site.urls),

    # Rotas para o Swagger UI
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),

    # Rotas para o ReDoc (opcional)
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

    # Rest Framework
    path('api-auth/', include('rest_framework.urls')),

    # Autenticação
    path('auth_ag/', include('auth_ag.urls')),

    # Apps API
    path('produtos/', include('produtos.urls')),
    path('estoque/', include('estoque.urls')),
    path('movimentos/', include('movimentos.urls')),

]
