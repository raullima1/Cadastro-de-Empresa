from django.db import models

class Empresa(models.Model):

    razao_social = models.CharField(max_length=80)
    nome_fantasia = models.CharField(max_length=80)
    cnpj = models.CharField(max_length=18)
    endereco = models.CharField(max_length=50)
    telefone = models.CharField(max_length=14)
    celular = models.CharField(max_length=14)
    email = models.CharField(max_length=30)
    site = models.CharField(max_length=30)

    def __str__ (self):
        return self.nome_fantasia
