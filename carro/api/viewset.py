from rest_framework.viewsets import ModelViewSet
from carro.api.filter import CarroFilter
from carro.api.serializer import CarroSerializer
from carro.models import Carro


class CarroViewSet(ModelViewSet):
    queryset = Carro.manager.all()
    serializer_class = CarroSerializer
    filterset_class = CarroFilter
