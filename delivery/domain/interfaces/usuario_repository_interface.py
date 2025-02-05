from abc import ABC, abstractmethod


class UsuarioRepositoryInterface(ABC):
    """
    Interface para a camada de persistência de dados de usuários.
    """

    @abstractmethod
    def obter_por_id(self, usuario_id: int):
        """
        Obtém os dados de um usuário pelo ID.
        """
        pass
