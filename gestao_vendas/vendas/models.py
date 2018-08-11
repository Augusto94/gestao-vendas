from django.db import models

# Create your models here.
class Cliente(models.Model):
    nome = models.CharField(max_length=30, blank=True)
    apelido = models.CharField(max_length=30, blank=True)
    idade = models.IntegerField(null=True, blank=True)
    documento = models.CharField(max_length=20, blank=True, null=True)
    telefone = models.CharField(max_length=13, blank=True, null=True)

    def __str__(self):
        return self.apelido