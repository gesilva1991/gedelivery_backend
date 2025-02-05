from unittest.mock import MagicMock

import pytest
from domain.entities.usuario import Usuario
from domain.use_cases.obter_informacoes_usuario_use_case import \
    ObterInformacoesUsuarioUseCase


@pytest.fixture
def usuario_repository_mock():
    """Fixture para o mock do repositório de usuários"""
    mock = MagicMock()
    mock.obter_por_id.return_value = {
        "id": 1,
        "username": "usuario_teste",
        "email": "teste@dominio.com",
        "first_name": "Nome",
        "last_name": "Sobrenome",
    }
    return mock


def test_obter_informacoes_usuario(usuario_repository_mock):
    """Testa o caso de uso de obter informações do usuário"""
    # Criar o caso de uso com o mock
    use_case = ObterInformacoesUsuarioUseCase(usuario_repository_mock)

    # Executar o caso de uso
    usuario = use_case.executar(1)

    # Verificar os resultados
    assert isinstance(usuario, Usuario)
    assert usuario.id == 1
    assert usuario.username == "usuario_teste"
    assert usuario.email == "teste@dominio.com"
    assert usuario.first_name == "Nome"
    assert usuario.last_name == "Sobrenome"

    # Verificar se o repositório foi chamado com o ID correto
    usuario_repository_mock.obter_por_id.assert_called_once_with(1)
