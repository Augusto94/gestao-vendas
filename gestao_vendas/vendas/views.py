from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import VendaForm

# Create your views here.
@login_required
def vendas(request):
    return render(request, 'vendas.html')


def novaVenda(request):
    form = VendaForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('vendas')
    
    return render(request, 'venda_form.html', {'form': form})