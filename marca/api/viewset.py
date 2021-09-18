from rest_framework.viewsets import ModelViewSet
from marca.api.serializer import MarcaSerializer
from marca.models import Marca
from .filter import MarcaFilter


class MarcaViewSet(ModelViewSet):
    queryset = Marca.manager.all()
    serializer_class = MarcaSerializer
    filterset_class = MarcaFilter
    http_method_names = ['get', 'post', 'put', 'delete']
