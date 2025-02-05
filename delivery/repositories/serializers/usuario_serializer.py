# serializers.py
from django.contrib.auth.models import User
from repositories.models.usuario_models import UsuarioModel
from rest_framework import serializers


class RegistroUsuarioSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = UsuarioModel
        fields = ["id", "username", "password", "email", "first_name", "last_name"]

    def create(self, validated_data):
        user = UsuarioModel.objects.create_user(
            username=validated_data["username"],
            email=validated_data["email"],
            password=validated_data["password"],
        )
        return user
