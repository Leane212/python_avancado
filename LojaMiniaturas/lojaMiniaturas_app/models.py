from django.db import models

class Produto (models.Model):
    nome = models.CharField(max_length=50)
    preco = models.DecimalField(max_digits = 6, decimal_places = 2)
    descricao = models.TextField()
    codigo = models.IntegerField()
    video = models.TextField(null=True)
    data_cadastro = models.DateField(null=True)
    
    def __str__ (self):
        return self.nome
    
class Imagem (models.Model):
    nome = models.CharField(max_length=50)

    def __str__ (self):
        return self.nome

class Categoria(models.Model):
    nome = models.CharField(max_length=50)
    
    def __str__ (self):
        return self.nome

class Marca (models.Model):
    nome = models.CharField(max_length=20)
    
    def __str__ (self):
        return self.nome
class Desconto (models.Model):
    valor = models.DecimalField(max_digits = 6, decimal_places = 2)
    
    def __str__ (self):
        return self.nome

class Especificacao (models.Model):
    aviso = models.TextField()
    recomendacao = models.TextField()
    restricao = models.TextField()
    origem = models.TextField()
    
    def __str__ (self):
        return self.aviso