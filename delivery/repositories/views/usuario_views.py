from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.permissions import AllowAny
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from applications.services.usuario_service import UsuarioService
from repositories.implementations.usuario_repository_impl import UsuarioRepositoryImpl
from repositories.serializers import RegistroUsuarioSerializer
from rest_framework.permissions import IsAuthenticated


class RegistroUsuarioView(APIView):
    permission_classes = [AllowAny]  # Permite acesso público (não autenticado)

    def post(self, request):
        serializer = RegistroUsuarioSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()  # Cria o usuário
            return Response({"message": "Usuário criado com sucesso!"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class InicioView(APIView):
    permission_classes = [IsAuthenticated]  # A rota exige que o usuário esteja autenticado

    def get(self, request):
        # Recupera as informações do usuário autenticado
        user = request.user  # O usuário autenticado estará disponível através de `request.user`
        
        # Prepare as informações do usuário para enviar na resposta
        user_info = {
            "username": user.username,
            "email": user.email,
            "first_name": user.first_name,
            "last_name": user.last_name,
            # Adicione outros campos que você deseja retornar
        }
        
        return Response(user_info)
