import django_filters
from django.db.models import Q
from .models import Cliente

class ClienteFilter(django_filters.FilterSet):
    search = django_filters.CharFilter(method='filter_global', label="Pesquisar")

    class Meta:
        model = Cliente
        fields = []

    def filter_global(self, queryset, name, value):
        return queryset.filter(
            Q(titulo__icontains=value) | 
            Q(tags__nome__icontains=value)  # Busca pelo nome da tag associada
        ).distinct()  # Evita resultados duplicados devido ao ManyToMany
