from rest_framework.response import Response
from rest_framework.viewsets import ViewSet

from carro.api.service import CarroService


class CarroViewSet(ViewSet):

    service = CarroService()

    def retrieve(self, request, pk=None):
        pass

    def list(self, request, *args, **kwargs) -> Response:
        pass

    def create(self, request, *args, **kwargs) -> Response:
        pass

    def update(self, request, *args, **kwargs) -> Response:
        pass

    def destroy(self, request, *args, **kwargs):
        pass
