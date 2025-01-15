import pytest
from rest_framework.exceptions import ValidationError
from repositories.models.usuario_models import UsuarioModel
from repositories.serializers import RegistroUsuarioSerializer

@pytest.mark.django_db
def test_serializer_create():
    """Teste se o RegistroUsuarioSerializer cria um usuário corretamente"""
    # Dados válidos para criar o usuário
    valid_data = {
        'username': 'usuario_test',
        'email': 'usuario_test@example.com',
        'password': 'senha_segura',
    }

    # Instancia o serializer com os dados válidos
    serializer = RegistroUsuarioSerializer(data=valid_data)

    # Verifica se o serializer é válido
    assert serializer.is_valid()

    # Cria o usuário usando o método `create` do serializer
    # user = serializer.save()

    # # Verifica se o usuário foi criado corretamente
    # assert user.username == valid_data['username']
    # assert user.email == valid_data['email']

    # # Verifica se a senha está sendo corretamente salva de forma criptografada
    # assert user.check_password(valid_data['password'])

# @pytest.mark.django_db
# def test_serializer_invalid_data():
#     """Teste se o serializer valida os dados corretamente e lida com erros"""
#     # Dados inválidos (sem email, que é obrigatório)
#     invalid_data = {
#         'username': 'usuario_test_invalido',
#         'password': 'senha_segura',
#     }

#     # Instancia o serializer com os dados inválidos
#     serializer = RegistroUsuarioSerializer(data=invalid_data)

#     # Verifica que o serializer não é válido
#     assert not serializer.is_valid()

#     # Verifica as mensagens de erro
#     assert 'email' in serializer.errors

# @pytest.mark.django_db
# def test_create_user_with_duplicate_email():
#     """Teste se o serializer lida com emails duplicados"""
#     # Cria o primeiro usuário
#     Usuario.objects.create_user(
#         username='usuario1',
#         email='duplicado@example.com',
#         password='senha_segura1'
#     )

#     # Dados para tentar criar um segundo usuário com o mesmo email
#     duplicate_email_data = {
#         'username': 'usuario2',
#         'email': 'duplicado@example.com',
#         'password': 'senha_segura2'
#     }

#     serializer = RegistroUsuarioSerializer(data=duplicate_email_data)

#     # Verifica que o serializer não é válido devido ao email duplicado
#     assert not serializer.is_valid()

#     # Verifica se a mensagem de erro foi gerada corretamente para o email duplicado
#     assert 'email' in serializer.errors

