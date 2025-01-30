import django_filters # type: ignore
from .models import Cliente


class ClienteFilter(django_filters.FilterSet):
    tags = django_filters.CharFilter(lookup_expr='icontains')
    titulo = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Cliente
        fields = '__all__'

        exclude = ['data_criacao','imagem']