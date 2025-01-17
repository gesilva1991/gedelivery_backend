SHELL := /bin/bash

# Comando para iniciar servidor Django
r:
	python manage.py runserver

da:
	daphne config.asgi:application

mk:
	python manage.py makemigrations

mg:
	python manage.py migrate


c:
	python manage.py collectstatic --noinput