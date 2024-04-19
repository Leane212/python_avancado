from django.db import models

class Produto (models.Model):
    nome = models.CharField(max_length=50)
    preco = models.DecimalField(max_digits = 6, decimal_places = 2)
    descricao = models.TextField()
    codigo = models.IntegerField()
    video = models.TextField()
    data_cadastro = models.DateField()
    marca = models.ForeignKey("Marca", on_delete=models.CASCADE)
    categoria = models.ForeignKey("Categoria", on_delete=models.CASCADE)

    def str (self):
        return self.nome
    
class Imagem (models.Model):
    nome = models.CharField(max_length=50)
    produto = models.ForeignKey("Produto", on_delete=models.CASCADE, related_name='imagens')
    
    def str (self):
        return self.nome

class Categoria(models.Model):
    nome = models.CharField(max_length=50)
    
    def str (self):
        return self.nome

class Marca(models.Model):
    nome = models.CharField(max_length=20)
    
    def str (self):
        return self.nome
class Desconto (models.Model):
    valor = models.DecimalField(max_digits = 6, decimal_places = 2)
    data_inicial = models.DateTimeField()
    data_final = models.DateTimeField()
    produto = models.ForeignKey("Produto", on_delete=models.CASCADE)
    
    def str (self):
        return self.valor

class Especificacao (models.Model):
    nome = models.CharField(max_length=20)
    descricao = models.TextField()
    produto = models.ForeignKey("Produto", on_delete=models.CASCADE)
    
    def str (self):
        return self.nome