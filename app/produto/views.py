from django.http import Http404
from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Produto, Categoria
from .serializers import ProdutoSerializer, CategoriaSerializer


class ProdutoList(APIView):
    def get(self, request):
        produto = Produto.objects.all()
        serializer = ProdutoSerializer(produto, many=True)
        print(serializer)

        return Response(serializer.data)

    def post(self, request):
        serializer = ProdutoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        else:
            return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)


class ProdutoMethodObject(APIView):
    def get_object(self, id):
        try:
            return Produto.object.get(id=id)

        except:
            raise Http404

    # pegar
    def get(self, request, id):
        produto = self.get_object(id)
        serializer = ProdutoSerializer(produto)

        return Response(serializer.data)

    # edicao
    def put(self, request, id):
        produto = self.get_object(id)
        serializer = ProdutoSerializer(produto, data=request.data)
        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data)

        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # apagar
    def delete(self, request, id):
        produto = self.get_object(id)
        produto.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)


class CategoriaList(APIView):

    def get(self, request):
        categoria = Categoria.objects.all()
        serializer = CategoriaSerializer(categoria, many=True)
        print(serializer)

        return Response(serializer.data)

    def post(self, request):
        serializer = CategoriaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        else:
            return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)


class CategoriaMethodObject(APIView):
    def get_object(self, id):
        try:
            return Categoria.object.get(id=id)

        except:
            raise Http404

    # pegar
    def get(self, request, id):
        categoria = self.get_object(id)
        serializer = CategoriaSerializer(categoria)

        return Response(serializer.data)

    # edicao
    def put(self, request, id):
        categoria = self.get_object(id)
        serializer = CategoriaSerializer(categoria, data=request.data)
        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data)

        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # apagar
    def delete(self, request, id):
        categoria = self.get_object(id)
        categoria.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)
from django.shortcuts import render

# Create your views here.
