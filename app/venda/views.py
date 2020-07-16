from django.shortcuts import render

# Create your views here.
from django.http import Http404
from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Venda, VendasProduto
from .serializers import VendaSerializer, VendasProdutoSerializer


class VendaList(APIView):
    def get(self, request):
        venda = Venda.objects.all()
        serializer = VendaSerializer(venda, many=True)
        print(serializer)

        return Response(serializer.data)

    def post(self, request):
        serializer = VendaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        else:
            return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)


class VendaMethodObject(APIView):
    def get_object(self, id):
        try:
            return Venda.object.get(id=id)

        except:
            raise Http404

    # pegar
    def get(self, request, id):
        venda = self.get_object(id)
        serializer = VendaSerializer(venda)

        return Response(serializer.data)

    # edicao
    def put(self, request, id):
        venda = self.get_object(id)
        serializer = VendaSerializer(venda, data=request.data)
        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data)

        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # apagar
    def delete(self, request, id):
        venda = self.get_object(id)
        venda.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)


class VendasProdutoList(APIView):

    def get(self, request):
        vendasproduto = VendasProduto.objects.all()
        serializer = VendasProdutoSerializer(vendasproduto, many=True)
        print(serializer)

        return Response(serializer.data)

    def post(self, request):
        serializer = VendasProdutoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        else:
            return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)


class VendasProdutoMethodObject(APIView):
    def get_object(self, id):
        try:
            return VendasProduto.object.get(id=id)

        except:
            raise Http404

    # pegar
    def get(self, request, id):
        vendasproduto = self.get_object(id)
        serializer = VendasProdutoSerializer(vendasproduto)

        return Response(serializer.data)

    # edicao
    def put(self, request, id):
        vendasproduto = self.get_object(id)
        serializer = VendasProdutoSerializer(vendasproduto, data=request.data)
        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data)

        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # apagar
    def delete(self, request, id):
        vendasproduto = self.get_object(id)
        vendasproduto.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)

