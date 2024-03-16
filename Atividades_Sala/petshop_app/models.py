from django.db import models

# Create your models here.
class Pets(models.Model):
    nomeAnimal = models.CharField(max_length=200)  #numero max caract
    raca = models.CharField(max_length=20)
    dataNascimento = models.DateField()

    def __str__(self):
        return self.nomeAnimal
    
    



