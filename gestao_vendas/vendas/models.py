from django.db import models
from datetime import datetime
import django

# Create your models here.
class Cliente(models.Model):
    nome = models.CharField(max_length=30, blank=True)
    apelido = models.CharField(max_length=30, blank=True)
    idade = models.IntegerField(null=True, blank=True)
    documento = models.CharField(max_length=20, blank=True, null=True)
    telefone = models.CharField(max_length=13, blank=True, null=True)

    def __str__(self):
        return self.apelido


class Venda(models.Model):
    data = models.DateTimeField(default=django.utils.timezone.now(), blank=True)
    peso = models.IntegerField(blank=True)

    ATIVA = 'ATIVA'
    ENCERRADA = 'ENCERRADA'

    STATUS_CHOICES = (
        (ATIVA, 'Ativa'),
        (ENCERRADA, 'Encerrada'),
    )
    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default=ATIVA,
    )

    valor = models.DecimalField(max_digits=5, decimal_places=2)
    cliente = models.ForeignKey(Cliente, on_delete=models.PROTECT)

    def __str__(self):
        return self.cliente.apelido + " " + str(self.data)