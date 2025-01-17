SHELL := /bin/bash

#Comando para gerar arquivo requirements.txt de pacotes instalados manualmente excluindo pacote de desenvolvimento
req:
	@pip list --not-required --format=freeze | grep -v -f <(tail -n +3 requirements-dev.txt) > requirements.txt
	@echo Arquivo Gerado

#Comando para gerar arquivo requirements.txt excluindo pacote de desenvolvimento
r:
	@pip list --format=freeze | grep -v -f <(tail -n +3 requirements-dev.txt) > requirements.txt
	@echo Arquivo Gerado


# Comando para listar apenas pacotes instalado explicitamente pelo programador
pip-list:
	pip list --not-required
 
# Comando para criar aplicativo Django - Substituir myapp pelo no nome do aplicativos
create:
	python manage.py startapp myapp

# Comando para iniciar servidor Django
run:
	cd ./delivery && \
	python manage.py runserver

test:
	python manage.py test

upgrade:	
	python3 -m pip install --upgrade pip

# python manage.py startapp myapp
# python manage.py collectstatic
# python manage.py makemigrations
# python manage.py migrate

# Verificar conexao
# npx wscat -c ws://localhost:8000/ws/pedidos/

# Subir server
# daphne -b 0.0.0.0 -p 8000 delivery.asgi:application

# ngrok http 5173