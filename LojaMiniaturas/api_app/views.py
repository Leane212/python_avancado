from django.shortcuts import render
from rest_framework.decorators import api_view
from lojaMiniaturas_app.models import Categoria
from api_app.serializers import CategoriaSerializer
from rest_framework.response import Response
from rest_framework import status
# Create your views here.
#dentro de @api_view recebe uma lista de métodos que quero permitir acesso
#many=true para pegar uma lista de categorias (todos os objetos de categoria) (many é muitos)
#serialize converte um objeto em texto json
@api_view(['GET', 'POST'])
def categoria (request):
    if request.method == "POST":
        serializer = CategoriaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    elif request.method == "GET":
        categorias = Categoria.objects.all()
        serializer = CategoriaSerializer(categorias,many=True)
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
        return Response(serializer.data, status=status.HTTP_204_NO_CONTENT)
    
