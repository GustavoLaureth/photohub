from django.shortcuts import redirect, render
from .form import ClienteForm, Cliente
from .filters import ClienteFilter
import random
from collections import defaultdict
from .models import Tag, Cliente

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

def explorer(request):
    clientes = Cliente.objects.prefetch_related('tags').all()

    tags_dict = defaultdict(list)

    for cliente in clientes:
        for tag in cliente.tags.all():
            tags_dict[tag.id].append(cliente)
        
    tags_com_imagem = []
    for tag_id, clientes_da_tag in tags_dict.items():
        if clientes_da_tag:
            cliente_aleatorio = random.choice(clientes_da_tag)
            tags_com_imagem.append({
                'tag': clientes_da_tag[0].tags.get(id=tag_id),
                'imagem': cliente_aleatorio.imagem.url if cliente_aleatorio.imagem else None,
            })
    
    return render(request, "hub/explorer.html", {'tags_com_imagem': tags_com_imagem,})