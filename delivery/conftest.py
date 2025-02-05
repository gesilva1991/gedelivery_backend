import os
import sys

import django
import pytest
from django.db import connections

# Adiciona o diretório do projeto ao sys.path para que o Django consiga encontrar as configurações
sys.path.append(
    os.path.join(os.path.dirname(__file__), "delivery")
)  # Ajuste para o caminho correto

os.environ["DJANGO_SETTINGS_MODULE"] = (
    "config.settings"  # Ajuste para o seu arquivo settings.py
)
django.setup()
