from django.db import models
'''
Importante para o funcionamento do 
AUTH_USER_MODEL = "repositories.UsuarioModel" em settings.py
'''
from .usuario_models import UsuarioModel
from .pedido_models import ProdutoModel