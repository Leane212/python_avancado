from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from lojaMiniaturas_app.models import Categoria, Produto
from rest_framework.exceptions import NotFound
from api_app.serializers import CategoriaSerializer, ProdutoSerializer
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
#dentro de @api_view recebe uma lista de métodos que quero permitir acesso
#many=true para pegar uma lista de categorias (todos os objetos de categoria) (many é muitos)
#serialize converte um objeto em texto json

class GetPostCategoriaView (APIView):
    def get (self, request):
        if request.user.is_authenticated and 'lojaMiniatura_app.wiew_item' in request.user.get_all_permissions():
            categorias = Categoria.objects.all()
            serializer = CategoriaSerializer(categorias,many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post (self, request):
        serializer = CategoriaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class GetPutDeleteCategoriaView (APIView):
    def get_object (self, request, id):
        try:
            return Categoria.objects.get(id=id)
        except Categoria.DoesNotExist:
            raise NotFound()
        
    def get (self, request, id):
        categoria = self.get_object(categoria)
        serializer = CategoriaSerializer(categoria)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def put (self, request, id):
        categoria = self.get_object(categoria)
        serializer = CategoriaSerializer(instance=categoria, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete (self, request, id):
        categoria = self.get_object(categoria)
        categoria.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

#CRIANDO VIEW QUE PEGA TABELA COM CHAVE ESTRANGEIRA UTILIZANDO DECORATIONS
@api_view(['GET', 'POST'])
def produto (request):
    if request.method == "POST":
        serializer = ProdutoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    elif request.method == "GET":
        produtos = Produto.objects.all()
        serializer = CategoriaSerializer(produtos,many=True)
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

'''@api_view(['GET', 'POST'])
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
    return Response(serializer.data, status=status.HTTP_200_OK)


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
        return Response(status=status.HTTP_204_NO_CONTENT)'''

   

    
    
