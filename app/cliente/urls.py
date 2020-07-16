from django.urls import path
from .views import ClientList, ClienteMethodObject, EnderecoList, EnderecoMethodObject

urlpatterns = [
    path('clientes/', ClientList.as_view()),
    path('cliente/<int:id>', ClienteMethodObject.as_view()),
    path('enderecos/', EnderecoList.as_view()),
    path('endereco/<int:id>', EnderecoMethodObject.as_view()),

]