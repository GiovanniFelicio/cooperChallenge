from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK
from rest_framework.viewsets import ViewSet

from marca.api.serializer import MarcaSerializer
from marca.api.service import MarcaService


class MarcaViewSet(ViewSet):

    service = MarcaService()

    def retrieve(self, request, pk=None):
        pass

    def list(self, request: Request, *args, **kwargs) -> Response:

        origem: str = request.query_params.get('origem') or ''
        nome: str = request.query_params.get('nome') or ''

        qs = self.service.find_by_origem_and_contains_nome(origem, nome)

        serializer = MarcaSerializer(qs, many=True)

        return Response(serializer.data, status=HTTP_200_OK)

    def create(self, request, *args, **kwargs) -> Response:
        pass

    def update(self, request, *args, **kwargs) -> Response:
        pass

    def destroy(self, request, *args, **kwargs):
        pass
