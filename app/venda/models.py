from django.db import models

# Create your models here.
from django.db import models


# Create your models here.
class Venda(models.Model):
    funcionario = models.ForeignKey('funcionario.Funcionario', on_delete=models.CASCADE)
    cliente = models.ForeignKey('cliente.Cliente', on_delete=models.CASCADE)
    criado_em = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name = 'Venda'
        verbose_name_plural = 'Vendas'

    def __str__(self):
        return 'Venda de {}'.format(self.funcionario)


class VendasProduto(models.Model):
    venda = models.ForeignKey(Venda, on_delete=models.CASCADE)
    produto = models.ForeignKey('produto.Produto', models.CASCADE)
    quantidade = models.PositiveIntegerField(null=True, default=1)

    class Meta:
        verbose_name = 'Produto da venda'
        verbose_name_plural = 'Produtos da venda'

    def __str__(self):
        return '{}'.format(self.venda)

