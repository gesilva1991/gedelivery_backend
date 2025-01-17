FROM python:3.13

# Impede a criação de arquivos .pyc (bytecode) no contêiner
# Isso ajuda a evitar o acúmulo de arquivos desnecessários e melhora o desempenho do build
ENV PYTHONDONTWRITEBYTECODE 1

# Configura a saída do Python para ser não-bufada
# Isso significa que as saídas do Python, como prints, serão enviadas diretamente para o console
# Isso é útil para depuração em tempo real no Docker
ENV PYTHONUNBUFFERED 1

WORKDIR /home

# Copiar o arquivo requirements.txt e instalar dependências
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copiar o restante do código da aplicação
COPY . .

WORKDIR /home/delivery

EXPOSE 8000

# Comando para iniciar o servidor
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
