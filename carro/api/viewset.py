from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from carro.api.filter import CarroFilter
from carro.api.serializer import CarroSerializer, CarroDetailSerializer
from carro.models import Carro


class CarroViewSet(ModelViewSet):
    queryset = Carro.manager.all()
    serializer_class = CarroSerializer
    filterset_class = CarroFilter

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = CarroDetailSerializer(instance)
        return Response(serializer.data)
