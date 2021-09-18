from rest_framework.viewsets import ModelViewSet

from carro.api.serializer import CarroSerializer
from carro.models import Carro


class CarroViewSet(ModelViewSet):
    queryset = Carro.objects.all()
    serializer_class = CarroSerializer
