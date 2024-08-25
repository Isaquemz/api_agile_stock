import jwt
from django.conf import settings
from django.http import JsonResponse
from .models import Usuario
from .views import autenticacao

def authenticate_token(view_func):
    def wrapper(request, *args, **kwargs):
        
        # Verifica se o token foi enviado na requisição
        try:
            token = args[0].headers.get('Authorization', '').split(' ')[1]
        except:
            return JsonResponse({'error': 'Invalid token'}, status=401)
        
        # Verifica se Token existe na tabela de gestão e se esta valido
        token_is_valid = autenticacao.is_valid_token(token)

        # Se for um token valido, atualiza informação no request.
        if token_is_valid:
            try:
                payload = jwt.decode(token, settings.SECRET_KEY, algorithms=['HS256'])
                user_id = payload['user_id']
                user = Usuario.objects.get(pk=user_id)
                args[0].user = user
            except jwt.ExpiredSignatureError:
                return JsonResponse({'error': 'Token has expired'}, status=401)
            except (jwt.InvalidTokenError, Usuario.DoesNotExist):
                return JsonResponse({'error': 'Invalid token'}, status=401)
            except:
                return JsonResponse({'error': 'Não foi possivel autenticar'}, status=400)
            
            return view_func(request, *args, **kwargs)
        else:
            return JsonResponse({'error': 'Invalid token'}, status=401)
    
    return wrapper