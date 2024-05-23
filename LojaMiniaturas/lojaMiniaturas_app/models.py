from django.db import models
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.urls import reverse

class Produto (models.Model):
    nome = models.CharField(max_length=50)
    preco = models.DecimalField(max_digits = 6, decimal_places = 2)
    descricao = models.TextField()
    codigo = models.IntegerField()
    video = models.TextField()
    data_cadastro = models.DateField(auto_now_add=True)
    marca = models.ForeignKey("Marca", on_delete=models.CASCADE)
    categoria = models.ForeignKey("Categoria", on_delete=models.CASCADE)
    especificacao = models.TextField()
    

    def __str__ (self):
        return self.nome
    
class Imagem (models.Model):
    nome = models.CharField(max_length=50)
    produto = models.ForeignKey("Produto", on_delete=models.CASCADE)
    
    def __str__ (self):
        return self.nome

class Categoria(models.Model):
    nome = models.CharField(max_length=50)
    
    def __str__ (self):
        return self.nome

class Marca(models.Model):
    nome = models.CharField(max_length=20)
    
    def __str__ (self):
        return self.nome
class Desconto (models.Model):
    valor = models.DecimalField(max_digits = 6, decimal_places = 2)
    data_inicial = models.DateTimeField()
    data_final = models.DateTimeField()
    produto = models.ForeignKey("Produto", on_delete=models.CASCADE)
    
    def __str__ (self):
        return self.valor
    
class MensagemContato(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    assunto = models.CharField(max_length=255)
    mensagem = models.TextField()
    data_envio = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.assunto
    
class Usuario (User):
    cpf = models.CharField(max_length=15)
    matricula = models.CharField(max_length=15, blank=True, null=True)
    
    def __str__ (self):
        return self.first_name + self.last_name


    

