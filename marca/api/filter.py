from django_filters import rest_framework as filters
from marca.models import Marca


class MarcaFilter(filters.FilterSet):
    nome = filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Marca
        fields = ('nome', 'origem')
