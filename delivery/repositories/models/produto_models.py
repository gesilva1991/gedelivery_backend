from django.db import models

class ProdutoModel(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome do Produto")
    descricao = models.TextField(verbose_name="Descrição")
    preco = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Preço")
    imagem = models.ImageField(upload_to='produtos/', blank=True, null=True, verbose_name="Imagem")

    def __str__(self):
        return self.nome
    
    class Meta:
        verbose_name = 'Produto'
        verbose_name_plural = "Produtos"
        db_table = 'produtos'
