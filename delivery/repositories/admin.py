from django.conf import settings
from django.contrib import admin

from .models.pedido_models import PedidoModel
from .models.produto_models import ProdutoModel
from .models.usuario_models import UsuarioModel

admin.site.site_header = settings.ADMIN_SITE_HEADER
admin.site.site_title = settings.ADMIN_SITE_TITLE
admin.site.index_title = settings.ADMIN_INDEX_TITLE

# admin.site.register(Usuario)


@admin.register(UsuarioModel)
class UsuarioAdmin(admin.ModelAdmin):
    pass


@admin.register(ProdutoModel)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ("nome", "preco")


@admin.register(PedidoModel)
class PedidoAdmin(admin.ModelAdmin):
    # list_display = ['id', 'cliente', 'status', 'data_criacao', 'data_atualizacao']
    # list_filter = ['status', 'cliente']
    pass
