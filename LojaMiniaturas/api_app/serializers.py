from rest_framework import serializers
from lojaMiniaturas_app.models import Categoria

class CategoriaSerializer (serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = ['id', 'nome']