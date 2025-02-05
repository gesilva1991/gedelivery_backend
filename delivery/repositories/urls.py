from django.urls import path
from repositories.views.usuario_views import InicioView, RegistroUsuarioView

urlpatterns = [
    path("registrar/", RegistroUsuarioView.as_view(), name="registrar_usuario"),
    path("inicio/", InicioView.as_view(), name="inicio"),  # Rota de início
]
