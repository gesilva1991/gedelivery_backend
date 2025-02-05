from django.conf import settings
from django.contrib.auth.models import User
from django.db import models
from repositories.models.produto_models import ProdutoModel


# Status do pedido
class StatusPedido(models.TextChoices):
    PENDENTE = "Pendente"
    EM_PROCESSAMENTO = "Em Processamento"
    CONCLUIDO = "Concluído"
    CANCELADO = "Cancelado"


# Modelo para representar um pedido
class PedidoModel(models.Model):
    cliente = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE
    )  # Relacionando o pedido a um cliente (usuário)
    endereco = models.CharField(max_length=255)  # Endereço de entrega do pedido
    status = models.CharField(
        max_length=20, choices=StatusPedido.choices, default=StatusPedido.PENDENTE
    )
    data_criacao = models.DateTimeField(auto_now_add=True)  # Data de criação do pedido
    data_atualizacao = models.DateTimeField(
        auto_now=True
    )  # Data de última atualização do pedido
    itens = models.JSONField(default=dict)

    def __str__(self):
        return f"Pedido #{self.id} - {self.cliente.username}"

    class Meta:
        verbose_name = "Pedido"
        verbose_name_plural = "Pedidos"
        db_table = "pedidos"
