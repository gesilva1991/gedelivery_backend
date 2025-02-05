from django.http import HttpResponse
from django.shortcuts import redirect
from django.utils.http import urlsafe_base64_encode
from django.conf import settings

def set_access_token(request):
    # Gerar o token (pode ser um JWT ou qualquer outro tipo de token)
    token = 'seu_token_de_acesso'

    response = HttpResponse('Token armazenado com sucesso!')

    # Configurando o cookie HttpOnly
    response.set_cookie(
        'access_token',
        token,
        httponly=True,
        secure=True,
        samesite='Strict',
        max_age=3600  # 1 hora
    )

    return response

def logout(request):
    # Remover o cookie de logout
    response = HttpResponse('Você foi desconectado.')
    response.delete_cookie('access_token')  # Apaga o cookie de acesso
    return response
