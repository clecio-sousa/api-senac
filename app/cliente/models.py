from django.db import models

# Create your models here.
from django.db import models


# Create your models here.
class Endereco(models.Model):
    endereco = models.CharField(max_length=100)
    bairro = models.DateTimeField(max_length=100)
    cidade = models.CharField(max_length=100)
    uf = models.CharField(max_length=100)
    latitude = models.FloatField()
    longitude = models.FloatField()

    class Meta:
        verbose_name = 'Endereço'
        verbose_name_plural = 'Endereços'

    def __str__(self):
        return '{}'.format(self.logradouro)


class Cliente(models.Model):
    SEXO_CHOICE = [
        (1, 'Masculino'),
        (2, 'Feminino')

    ]
    TIPO_CHOICE = [
        (1, 'Pessoa Física'),
        (2, 'Pessoa Jurídica')
    ]

    nome = models.CharField(max_length=100)
    sexo = models.IntegerField(choices=SEXO_CHOICE)
    data_nascimento = models.DateField(auto_now=False)
    endereco = models.ForeignKey(Endereco, on_delete=models.CASCADE)
    telefone = models.CharField(max_length=25)
    tipo = models.IntegerField(choices=TIPO_CHOICE)

    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'

    def __str__(self):
        return '{}'.format(self.nome_cliente)
