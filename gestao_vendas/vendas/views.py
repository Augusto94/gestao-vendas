from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import VendaForm
from .models import Cliente, Venda

# Create your views here.
@login_required
def vendas(request):
    return render(request, 'vendas.html')


@login_required
def novaVenda(request):
    form = VendaForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('vendas')
    
    return render(request, 'venda_form.html', {'form': form})


@login_required
def listVendas(request):
    vendas = Venda.objects.all()
    for venda in vendas:
        venda = venda.__dict__
        venda['valor'] = float(venda['valor'])
        venda['cliente'] = Cliente.objects.get(id=venda['cliente_id']).apelido
        venda['comissao'] = round(venda['valor'] * 0.05, 2)
    return render(request, 'all_vendas.html', {'vendas': vendas})


@login_required
def updateVenda(request, id):
    venda = get_object_or_404(Venda, pk=id)
    form = VendaForm(request.POST or None, instance=venda)
    if form.is_valid():
        form.save()
        return redirect('all_vendas')

    return render(request, 'venda_form.html', {'form': form})