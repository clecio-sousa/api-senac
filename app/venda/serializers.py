from rest_framework import serializers

from .models import Venda, VendasProduto


class VendasProdutoSerializer(serializers.ModelSerializer):
    class Meta:
        model = VendasProduto
        fields = '__all__'


class VendaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Venda
        fields = '__all__'
