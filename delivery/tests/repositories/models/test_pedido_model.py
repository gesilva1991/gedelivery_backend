import pytest
from django.contrib.auth.models import User
from repositories.models.usuario_models import UsuarioModel 
from repositories.models.pedido_models import PedidoModel

@pytest.fixture
def usuario():
    # Criação de um usuário para os testes
    return UsuarioModel.objects.create(username='cliente', password='senha123')

@pytest.fixture
def pedido(usuario):
    # Criação de um pedido para os testes
    return PedidoModel.objects.create(
        cliente=usuario,
        status='pendente',
        itens={'produto':'lata'}
    )

@pytest.mark.django_db
def test_criar_pedido(pedido, usuario):
    # Testa a criação do pedido e valida os dados
    assert pedido.cliente == usuario  # Verifica se o cliente está correto
    assert pedido.status == 'pendente'  # Verifica o status do pedido

# def test_atualizar_status_pedido(pedido):
#     # Testa a atualização do status do pedido
#     pedido.status = 'finalizado'
#     pedido.save()

#     # Verifica se o status foi atualizado corretamente
#     assert pedido.status == 'finalizado'

# def test_str_metodo(pedido):
#     # Testa o método __str__ do modelo Pedido
#     str_pedido = str(pedido)
#     assert str_pedido == f"Pedido {pedido.id} - {pedido.cliente.username} - {pedido.status}"

