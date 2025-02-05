from domain.interfaces.usuario_repository_interface import \
    UsuarioRepositoryInterface
from repositories.models.usuario_models import UsuarioModel


class UsuarioRepositoryImpl(UsuarioRepositoryInterface):
    """
    Implementação do repositório de usuários utilizando o modelo Django.
    """

    def obter_por_id(self, usuario_id: int):
        try:
            usuario_obj = UsuarioModel.objects.get(id=usuario_id)
            return {
                "id": usuario_obj.id,
                "username": usuario_obj.username,
                "email": usuario_obj.email,
                "first_name": usuario_obj.first_name,
                "last_name": usuario_obj.last_name,
            }
        except UsuarioModel.DoesNotExist:
            return None
