from django.db import models

# Create your models here.
from django.db import models


# Create your models here.

class Setor(models.Model):
    TIPO_CHOICE = [
        (1, 'Vendas Externas'),
        (2, 'Vendas Internas')
    ]
    nome = models.CharField(max_length=100)
    tipo = models.IntegerField(choices=TIPO_CHOICE)

    class Meta:
        verbose_name = 'Setor'
        verbose_name_plural = 'Setores'

    def __str__(self):
        return '{}'.format(self.nome)


class Funcionario(models.Model):
    nome = models.CharField(max_length=100)
    data_nascimento = models.DateField(auto_now=False)
    cpf = models.PositiveIntegerField()
    setor = models.ForeignKey(Setor, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Funcionário'
        verbose_name_plural = 'Funcionários'

    def __str__(self):
        return '{}'.format(self.nome)