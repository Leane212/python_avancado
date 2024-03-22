from django.db import models

class Produtos (models.Model):
    nome = models.CharField(max_length=200)
    preco = models.DecimalField(max_digits = 6, decimal_places = 2)
    descricao = models.TextField()
    codigo = models.IntegerField()

    def __str__ (self):
        return self.nome
