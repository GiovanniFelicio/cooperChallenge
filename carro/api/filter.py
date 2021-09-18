from django_filters import rest_framework as filters
from carro.models import Carro


class CarroFilter(filters.FilterSet):
    nome = filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Carro
        fields = ('nome', 'origem')
