from django.urls import path
from .views import VendasProdutoList, VendasProdutoMethodObject, VendaList, VendaMethodObject

urlpatterns = [
    path('vendas/', VendaList.as_view()),
    path('venda/<int:id>', VendaMethodObject.as_view()),
    path('vendasprodutos/', VendasProdutoList.as_view()),
    path('vendaproduto/<int:id>', VendasProdutoMethodObject.as_view()),

]