from django.db import models

# Create your models here.
from django.db import models


# Create your models here.

class Categoria(models.Model):
    TIPO_CHOICE = [
        (1, 'Atacado'),
        (2, 'Varejo')
    ]
    nome = models.CharField(max_length=100)
    tipo_venda = models.IntegerField(choices=TIPO_CHOICE)

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'

    def __str__(self):
        return '{}'.format(self.nome)


class Produto(models.Model):
    nome = models.CharField(max_length=200)
    preco = models.DecimalField(max_digits=5, decimal_places=2)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    estoque = models.PositiveIntegerField()

    class Meta:
        verbose_name = 'Produto'
        verbose_name_plural = 'Produtos'

    def __str__(self):
        return '{}'.format(self.nome)