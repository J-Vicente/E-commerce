from django.db import models

# Create your models here.

class Product(models.Model):
    nome = models.CharField(max_length=150)
    preco = models.FloatField()
    descricao = models.TextField()
    imagem = models.ImageField(upload_to='images')
    
    def __str__(self):
        return self.nome
