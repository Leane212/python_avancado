from rest_framework import serializers
from lojaMiniaturas_app.models import Categoria, Produto

class CategoriaSerializer (serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = ['id', 'nome']
        
class ProdutoSerializer (serializers.ModelSerializer):
    class Meta:
        model = Produto
        fields = ['nome','preco','descricao','codigo','video','marca','categoria','especificacao']
