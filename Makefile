SHELL := /bin/bash

#Comando para gerar arquivo requirements.txt de pacotes instalados manualmente excluindo pacote de desenvolvimento
reqn:
	@pip list --not-required --format=freeze | grep -v -f <(tail -n +3 requirements-dev.txt) > requirements.txt
	@echo Arquivo Gerado

#Comando para gerar arquivo requirements.txt excluindo pacote de desenvolvimento
req:
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

lint:
	# flake8 .
	black .
	black --check .
	isort .
	isort --check-only .
	# pylint delivery/

# python manage.py startapp myapp
# python manage.py collectstatic
# python manage.py makemigrations
# python manage.py migrate

# Verificar conexao
# npx wscat -c ws://localhost:8000/ws/pedidos/

# Subir server asgi com daphne
# daphne config.asgi:application ou daphne -b 0.0.0.0 -p 8000 config.asgi:application

# Subir server wsgi com gunicorn
# gunicorn config.wsgi:application

# ngrok http 5173

# Para análise estática de código (verifica erros e inconsistências no estilo de código).
# flake8 .

# Para remover importações não utilizadas em todos os arquivos do seu projeto
# autoflake --in-place --remove-all-unused-imports --exclude=venv .

# Para verificão automática do código (estilo de código )
# black --check .

# Para formatação automática do código (estilo de código )
# black .

# Para organizar as importações de maneira ordenada
# isort --check-only .

# Para organizar as importações de maneira ordenada
# isort .

# Para checagem de tipos, caso você tenha tipagem estática no seu código
# mypy delivery/

# Para gerar um arquivo .pylintrc padrão, execute o seguinte comando
# pylint --generate-rcfile > .pylintrc

# Para análise estática de código Python que verifica o estilo e a qualidade do código, detectando erros, falhas de estilo, e possíveis melhorias. Ele segue as convenções do PEP 8 (e outras), e pode ser configurado para ajudar a manter o código mais limpo e consistente.
# pylint delivery/

# formata automaticamente o código Python para que ele siga as convenções do PEP 8 
# autopep8 --in-place --recursive delivery/





