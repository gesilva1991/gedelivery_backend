from domain.use_cases.obter_informacoes_usuario_use_case import ObterInformacoesUsuarioUseCase
from domain.interfaces.usuario_repository_interface import UsuarioRepositoryInterface

class UsuarioService:
    def __init__(self, usuario_repository_interface: UsuarioRepositoryInterface):
        self.usuario_repository_interface = usuario_repository_interface

    def obter_usuario_por_id(self, usuario_id: int):
        use_case = ObterInformacoesUsuarioUseCase(self.usuario_repository_interface)
        return use_case.executar(usuario_id)
