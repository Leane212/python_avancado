from django.contrib import admin
from lojaMiniaturas_app.models import Produto
from lojaMiniaturas_app.models import Imagem
from lojaMiniaturas_app.models import Categoria
from lojaMiniaturas_app.models import Marca
from lojaMiniaturas_app.models import Desconto


admin.site.register(Produto)
admin.site.register(Imagem)
admin.site.register(Categoria)
admin.site.register(Marca)
admin.site.register(Desconto)
