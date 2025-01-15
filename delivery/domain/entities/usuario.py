
class Usuario:
    """
    Entidade que representa um usuário do sistema.
    A entidade não se preocupa com persistência ou lógica de banco de dados.
    """
    def __init__(self, id: int, username: str, email: str, first_name: str, last_name: str):
        self.id = id
        self.username = username
        self.email = email
        self.first_name = first_name
        self.last_name = last_name

    def __repr__(self):
        return f"<Usuario {self.username} ({self.id})>"

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.username})"
