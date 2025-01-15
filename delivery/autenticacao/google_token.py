from google.auth.transport.requests import Request
from google.oauth2 import id_token
from google.auth import exceptions

def validate_google_token(id_token_received: str, client_id: str) -> dict:
    """
    Valida o token ID recebido do Google.

    :param id_token_received: O ID Token recebido do Google na autenticação.
    :param client_id: O Client ID do seu projeto no Google Cloud.
    :return: O payload do token se for válido.
    :raises: exceptions.GoogleAuthError se o token for inválido.
    """
    try:
        # Verifica o ID Token
        decoded_token = id_token.verify_oauth2_token(id_token_received, Request())
        return decoded_token
    except exceptions.GoogleAuthError as e:
        raise ValueError("Token inválido ou expirado") from e
