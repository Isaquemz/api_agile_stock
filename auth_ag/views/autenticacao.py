import jwt

from django.conf import settings
from datetime import datetime, timedelta

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

# Usuario
from auth_ag.serializers import UsuarioSerializer
from auth_ag.models import Usuario

# Token
from auth_ag.models import Token

# Criptografar e Descriptografar
from .criptografia import descriptografar_dados


def is_valid_token(token):
        
    # Verifica se Token existe na tabela de gestão e se esta valido
    try:
        token_valid = Token.objects.get(de_token=token)
        if token_valid.dh_expiracao > datetime.now().astimezone(token_valid.dh_expiracao.tzinfo):
            return True
        else:
            return False
    except Token.DoesNotExist:
        return False


def generate_jwt_token(user):
    payload = {
        'user_id': user.co_usuario,
        'username': user.de_nome_usuario,
        'email': user.de_email,
        'profile': user.co_perfil.co_perfil,
        'exp': datetime.now() + timedelta(days=1)
    }
    token = jwt.encode(payload, settings.SECRET_KEY, algorithm='HS256')
    return token, payload


class LoginAPIView(APIView):

    @staticmethod
    def post(self, request):
            
        serializer = UsuarioSerializer(data=request.data, partial = True)

        if serializer.is_valid():

            if serializer.validated_data != {} and \
                'de_nome_usuario' in serializer.validated_data and \
                    'de_senha' in serializer.validated_data:

                # Busca todos os usuarios
                users = Usuario.objects.all()

                # Verifica usuario por usuario, decodificando a senha, se o usuario e senha existem.
                for user in users:
                    if user.de_nome_usuario == serializer.validated_data['de_nome_usuario'] and \
                            str(descriptografar_dados(user.de_senha).decode()) == serializer.validated_data['de_senha']:
                        user_find = user.co_usuario

                # Tenta pegar o usuario
                try:
                    user = Usuario.objects.get(co_usuario=user_find)
                except:
                    user = None

                # Usuario encontrado, gera token
                if user is not None and user.ic_ativo == 1:
                    
                    # Atualiza ultimo login
                    user.dh_ultimo_login = datetime.now()
                    user.save()

                    # Gera token com informações
                    token, payload = generate_jwt_token(user)

                    # Salvar Token em tabela
                    token_save = Token()
                    token_save.co_usuario = user
                    token_save.co_perfil = user.co_perfil
                    token_save.dh_expiracao = payload['exp']
                    token_save.de_token = token
                    token_save.save()

                    return Response({'token': token}, status=status.HTTP_200_OK)
                else:
                    return Response({'error': 'Credenciais incorretas ou inexistente'},
                                    status=status.HTTP_401_UNAUTHORIZED)
            else:
                return Response({'error': 'Campos obrigatorios não estão presentes (de_nome_usuario, de_senha)'},
                                status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LogoutAPIView(APIView):

    @staticmethod
    def get(self, request):

        try:
            token = request.headers.get('Authorization', '').split(' ')[1]
            if token is not None:
                token_save = Token.objects.get(de_token=token)
                token_save.dh_expiracao = datetime.now()
                token_save.save()
        except:
            pass

        return Response(status=status.HTTP_200_OK)


class ValidTokenAPIView(APIView):

    def get(self, request):

        try:
            token = request.headers.get('Authorization', '').split(' ')[1]
            if is_valid_token(token):
                return Response({'is_valid': True}, status=status.HTTP_200_OK)
            else:
                return Response({'is_valid': False}, status=status.HTTP_200_OK)
        except:
            return Response({'is_valid': False}, status=status.HTTP_200_OK)
