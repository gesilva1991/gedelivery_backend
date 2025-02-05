from autenticacao.google_token import validate_google_token
from config import settings
from django.contrib.auth import authenticate
from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from django.http import JsonResponse
from django.conf import settings
from rest_framework.response import Response



class LoginView(APIView):
    permission_classes = [AllowAny]  # Permite acesso público (não autenticado)

    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")

        user = authenticate(username=username, password=password)
        if user:
            refresh = RefreshToken.for_user(user)
            access_token = str(refresh.access_token)
            return Response({"access_token": access_token}, status=status.HTTP_200_OK)
        return Response(
            {"detail": "Credenciais inválidas."}, status=status.HTTP_401_UNAUTHORIZED
        )


class LogoutView(APIView):
    def post(self, request):
        # Invalidate the user's token here (client-side responsibility)
        return Response(
            {"detail": "Logout realizado com sucesso."}, status=status.HTTP_200_OK
        )


class AuthenticateWithGoogle(APIView):
    permission_classes = [AllowAny]  # Permite acesso público (não autenticado)

    def post(self, request):
        """
        Endpoint para autenticar com o Google e validar o ID Token.
        """
        id_token_received = request.data.get("id_token")

        if not id_token_received:
            return Response(
                {"error": "ID token não fornecido"}, status=status.HTTP_400_BAD_REQUEST
            )

        try:
            # Validando o ID Token recebido
            decoded_token = validate_google_token(
                id_token_received, settings.GOOGLE_CLIENT_ID
            )

            # Token válido, podemos retornar os dados do usuário ou outras ações
            return Response(
                {"message": "Token válido", "user_info": decoded_token},
                status=status.HTTP_200_OK,
            )

        except ValueError as e:
            return Response({"error": str(e)}, status=status.HTTP_401_UNAUTHORIZED)



class CheckCookieView(APIView):
    permission_classes = [AllowAny]  # Permite acesso público (não autenticado)

    def get(self, request):
        self.token = request.COOKIES.get('access_token')
        
        if not self.token:
            
            # Se o token não estiver no cookie, retorne um erro 401 Unauthorized
            return JsonResponse(
                {'detail': 'Token não encontrado no cookie. Autenticação necessária.'}, 
                status=401
            )

        return JsonResponse(
                {'detail': self.token}, 
                status=200
            )
    



class SetCookie(APIView):
    permission_classes = [AllowAny]  # Permite acesso público (não autenticado)

    def post(self, request):
        """
        Endpoint para salvar o cookie.
        """
        id_token_received = request.data.get('acessToken')

        if not id_token_received:
            return Response(
                {"error": "Token não fornecido"}, status=status.HTTP_400_BAD_REQUEST
            )

        try:
            # Validando o ID Token recebido
            decoded_token = validate_google_token(
                id_token_received, settings.GOOGLE_CLIENT_ID
            )
            response = Response({
                'message': 'Login successful',
                'accessToken': id_token_received,
            })

            response.set_cookie(
                key='access_token',
                value=id_token_received,
                httponly=True,  # Impede o acesso via JavaScript
                secure=False,    # Só funciona via HTTPS
                samesite='Strict',  # Impede o envio do cookie em contextos cross-site
                max_age=60*60  # Tempo de expiração (aqui está 1 hora)
            )

            # Token válido, podemos retornar os dados do usuário ou outras ações
            return Response(
                {"message": "Token válido", "user_info": decoded_token},
                status=status.HTTP_200_OK,
            )

        

        except ValueError as e:
            return Response({"error": str(e)}, status=status.HTTP_401_UNAUTHORIZED)



class Te(APIView):
    permission_classes = [AllowAny]  # Permite acesso público (não autenticado)

    async def post(self, request):
        """
        Endpoint para receber informações de usuários.
        """
        info_user = await request.json()
        print("info_user")

        # if not id_token_received:
        #     return Response(
        #         {"error": "Token não fornecido"}, status=status.HTTP_400_BAD_REQUEST
        #     )

        # try:
        #     # Validando o ID Token recebido
        #     decoded_token = validate_google_token(
        #         id_token_received, settings.GOOGLE_CLIENT_ID
        #     )
        #     response = Response({
        #         'message': 'Login successful',
        #         'accessToken': id_token_received,
        #     })

        #     response.set_cookie(
        #         key='access_token',
        #         value=id_token_received,
        #         httponly=True,  # Impede o acesso via JavaScript
        #         secure=False,    # Só funciona via HTTPS
        #         samesite='Strict',  # Impede o envio do cookie em contextos cross-site
        #         max_age=60*60  # Tempo de expiração (aqui está 1 hora)
        #     )

        #     # Token válido, podemos retornar os dados do usuário ou outras ações
        #     return Response(
        #         {"message": "Token válido", "user_info": decoded_token},
        #         status=status.HTTP_200_OK,
        #     )

        

        # except ValueError as e:
        #     return Response({"error": str(e)}, status=status.HTTP_401_UNAUTHORIZED)



