from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
from rest_framework import status
from autenticacao.google_token import validate_google_token
from config import settings



class LoginView(APIView):
    permission_classes = [AllowAny]  # Permite acesso público (não autenticado)
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        user = authenticate(username=username, password=password)
        if user:
            refresh = RefreshToken.for_user(user)
            access_token = str(refresh.access_token)
            return Response({"access_token": access_token}, status=status.HTTP_200_OK)
        return Response({"detail": "Credenciais inválidas."}, status=status.HTTP_401_UNAUTHORIZED)

class LogoutView(APIView):
    def post(self, request):
        # Invalidate the user's token here (client-side responsibility)
        return Response({"detail": "Logout realizado com sucesso."}, status=status.HTTP_200_OK)

class AuthenticateWithGoogle(APIView):
    permission_classes = [AllowAny]  # Permite acesso público (não autenticado)

    def post(self, request):
        """
        Endpoint para autenticar com o Google e validar o ID Token.
        """
        id_token_received = request.data.get("id_token")
        
        if not id_token_received:
            return Response({"error": "ID token não fornecido"}, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            # Validando o ID Token recebido
            decoded_token = validate_google_token(id_token_received, settings.GOOGLE_CLIENT_ID)

            
            # Token válido, podemos retornar os dados do usuário ou outras ações
            return Response({
                "message": "Token válido",
                "user_info": decoded_token
            }, status=status.HTTP_200_OK)
        
        except ValueError as e:
            return Response({"error": str(e)}, status=status.HTTP_401_UNAUTHORIZED)
        