from django.db import models
from django.contrib.auth.models import AbstractUser

class UsuarioModel(AbstractUser):
    telefone = models.CharField(max_length=15, blank=True, null=True)  
    endereco = models.CharField(max_length=255, blank=True, null=True)  
    data_nascimento = models.DateField(blank=True, null=True)  
    # data_criacao = ""
    # data_atualizacao = ""

    def __str__(self):
        return self.username  # Exibir o nome de usuário como representação
    
    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = "Usuarios"
        db_table = 'usuarios'
