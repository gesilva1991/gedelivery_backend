from domain.entities.usuario import Usuario


class ObterInformacoesUsuarioUseCase:
    """
    Caso de uso para obter informações de um usuário.
    """

    def __init__(self, usuario_repository: Usuario):
        self.usuario_repository = usuario_repository

    def executar(self, usuario_id: int) -> Usuario:
        """
        Obtém as informações do usuário a partir do ID.
        """
        usuario_data = self.usuario_repository.obter_por_id(usuario_id)
        if usuario_data:
            return Usuario(
                id=usuario_data["id"],
                username=usuario_data["username"],
                email=usuario_data["email"],
                first_name=usuario_data["first_name"],
                last_name=usuario_data["last_name"],
            )
        else:
            raise ValueError(f"Usuário com ID {usuario_id} não encontrado.")
