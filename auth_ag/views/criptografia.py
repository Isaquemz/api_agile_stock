from cryptography.fernet import Fernet
from django.conf import settings
import base64

# Obtém a SECRET_KEY do projeto Django e a converte para bytes
chave_str = settings.SECRET_KEY
# Codifica a chave em bytes usando UTF-8
chave_bytes = chave_str.encode('utf-8')
# Se a chave for maior que 32 bytes, trunque-a para 32 bytes
chave_bytes = chave_bytes[:32]
# Se a chave for menor que 32 bytes, preencha-a com espaços em branco até atingir 32 bytes
chave_bytes = chave_bytes.ljust(32, b' ')
# Codifica a chave para base64
chave_base64 = base64.urlsafe_b64encode(chave_bytes)

# Função para criptografar dados
def criptografar_dados(dados):
    f = Fernet(chave_base64)
    dados = f.encrypt(dados.encode())
    dados = str(str(dados).replace("b'", "")).replace("'", "")
    return dados

# Função para descriptografar dados
def descriptografar_dados(dados):
    f = Fernet(chave_base64)
    dados = f.decrypt(dados)
    return dados
