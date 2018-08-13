from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import VendaForm
from .models import Venda

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
    return render(request, 'all_vendas.html', {'vendas': vendas})