from django.contrib import admin
from django.urls import path
from .views import vendas, novaVenda, listVendas, updateVenda

urlpatterns = [
    path('', vendas, name='vendas'),
    path('nova-venda/', novaVenda, name='nova_venda'),
    path('lista-vendas/', listVendas, name='all_vendas'),
    path('update/<int:id>', updateVenda, name='update_venda'),
]
