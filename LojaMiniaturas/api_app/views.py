from django.shortcuts import render
from rest_framework.decorators import api_view
from lojaMiniaturas_app.models import Categoria, Produto
from api_app.serializers import CategoriaSerializer, ProdutoSerializer
from rest_framework.response import Response
from rest_framework import status



# Create your views here.


@api_view(['GET','POST'])
def categoria (request):
    if request.method == 'POST':
        serializer = CategoriaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "GET":
        categorias = Categoria.objects.all()
        serializer = CategoriaSerializer(categorias, many = True)
        return Response(serializer.data)
    
@api_view(['GET', 'PUT', 'DELETE'])
def categoria_id (request, id):
    try:
        categoria = Categoria.objects.get(id=id)
    except Categoria.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == "GET":
        serializer = CategoriaSerializer(categoria)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == "PUT":
        serializer = CategoriaSerializer(instance=categoria, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == "DELETE":
        categoria.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET','POST'])
def produto (request):
    if request.method == 'POST':
        serializer = ProdutoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "GET":
        produtos = Produto.objects.all()
        serializer = ProdutoSerializer(produtos, many = True)
        return Response(serializer.data) 
    
@api_view(['GET', 'PUT', 'DELETE'])
def produto_id (request, id):
    try:
        produto = Produto.objects.get(id=id)
    except Produto.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == "GET":
        serializer = ProdutoSerializer(produto)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == "PUT":
        serializer = ProdutoSerializer(instance=produto, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == "DELETE":
        produto.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)