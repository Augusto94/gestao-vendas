from django.contrib import admin
from django.urls import path
from .views import vendas, novaVenda

urlpatterns = [
    path('', vendas, name='vendas'),
    path('nova-venda/', novaVenda, name='nova_venda')
]
