# Dockerfile
FROM python:3.13

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /home/espetinho

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .