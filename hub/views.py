from django.shortcuts import redirect, render
from .form import ClienteForm, Cliente
from .filters import ClienteFilter
from django.core.paginator import Paginator

def hub(request):
    list_clientes = Cliente.objects.order_by('-data_criacao')
    myFilter = ClienteFilter(request.GET, queryset=list_clientes)
    list_clientes = myFilter.qs
    
    return render(request, "hub/hub.html", {'clientes': list_clientes, 'myFilter': myFilter})

def form(request):
    data = {}
    data['form'] = ClienteForm()
    return render(request, 'hub/form.html', data)

def create(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('hub')
    else:
        form = ClienteForm()
    
def edit(request, pk):
    cliente = Cliente.objects.get(pk=pk)
    form = ClienteForm(instance=cliente)
    return render(request, 'hub/form.html', {'cliente': cliente, 'form': form})

def detalhe(request, pk):
    cliente = Cliente.objects.get(pk=pk)
    return render(request, 'hub/detalhe.html', {'hub': cliente})

def update(request, pk):
    cliente = Cliente.objects.get(pk=pk)
    form = ClienteForm(request.POST, instance=cliente)
    if form.is_valid():
        form.save()
        return redirect('hub')
    
def delete(request, pk):
    cliente = Cliente.objects.get(pk=pk)
    cliente.delete()
    return redirect('hub')