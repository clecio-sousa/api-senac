from django.http import Http404
from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Cliente, Endereco
from .serializers import ClienteSerializer, EnderecoSerializer

# Create your views here.
'''
GET POST PUT DELETE
'''


class ClientList(APIView):
    def get(self, request):
        cliente = Cliente.objects.all()
        serializer = ClienteSerializer(cliente, many=True)
        print(serializer)

        return Response(serializer.data)

    def post(self, request):
        serializer = ClienteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        else:
            return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)


class ClienteMethodObject(APIView):
    def get_object(self, id):
        try:
            return Cliente.object.get(id=id)

        except:
            raise Http404

    # pegar
    def get(self, request, id):
        cliente = self.get_object(id)
        serializer = ClienteSerializer(cliente)

        return Response(serializer.data)

    # edicao
    def put(self, request, id):
        cliente = self.get_object(id)
        serializer = ClienteSerializer(cliente, data=request.data)
        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data)

        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # apagar
    def delete(self, request, id):
        cliente = self.get_object(id)
        cliente.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)


class EnderecoList(APIView):

    def get(self, request):
        endereco = Endereco.objects.all()
        serializer = EnderecoSerializer(endereco, many=True)
        print(serializer)

        return Response(serializer.data)

    def post(self, request):
        serializer = EnderecoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        else:
            return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)


class EnderecoMethodObject(APIView):
    def get_object(self, id):
        try:
            return Endereco.object.get(id=id)

        except:
            raise Http404

    # pegar
    def get(self, request, id):
        endereco = self.get_object(id)
        serializer = EnderecoSerializer(endereco)

        return Response(serializer.data)

    # edicao
    def put(self, request, id):
        endereco = self.get_object(id)
        serializer = EnderecoSerializer(endereco, data=request.data)
        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data)

        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # apagar
    def delete(self, request, id):
        endereco = self.get_object(id)
        endereco.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)
