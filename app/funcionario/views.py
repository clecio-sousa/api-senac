from django.http import Http404
from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Funcionario, Setor
from .serializers import FuncionarioSerializer, SetorSerializer


class FuncionarioList(APIView):
    def get(self, request):
        funcionario = Funcionario.objects.all()
        serializer = FuncionarioSerializer(funcionario, many=True)
        print(serializer)

        return Response(serializer.data)

    def post(self, request):
        serializer = FuncionarioSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        else:
            return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)


class FuncionarioMethodObject(APIView):
    def get_object(self, id):
        try:
            return Funcionario.object.get(id=id)

        except:
            raise Http404

    # pegar
    def get(self, request, id):
        funcionario = self.get_object(id)
        serializer = FuncionarioSerializer(funcionario)

        return Response(serializer.data)

    # edicao
    def put(self, request, id):
        funcionario = self.get_object(id)
        serializer = FuncionarioSerializer(funcionario, data=request.data)
        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data)

        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # apagar
    def delete(self, request, id):
        funcionario = self.get_object(id)
        funcionario.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)


class SetorList(APIView):

    def get(self, request):
        setor = Setor.objects.all()
        serializer = SetorSerializer(setor, many=True)
        print(serializer)

        return Response(serializer.data)

    def post(self, request):
        serializer = SetorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        else:
            return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)


class SetorMethodObject(APIView):
    def get_object(self, id):
        try:
            return Setor.object.get(id=id)

        except:
            raise Http404

    # pegar
    def get(self, request, id):
        setor = self.get_object(id)
        serializer = SetorSerializer(setor)

        return Response(serializer.data)

    # edicao
    def put(self, request, id):
        setor = self.get_object(id)
        serializer = SetorSerializer(setor, data=request.data)
        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data)

        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # apagar
    def delete(self, request, id):
        setor = self.get_object(id)
        setor.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)
