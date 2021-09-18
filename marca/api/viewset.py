from rest_framework.viewsets import ModelViewSet
from marca.api.serializer import MarcaSerializer
from marca.models import Marca


class MarcaViewSet(ModelViewSet):
    queryset = Marca.objects.all()
    serializer_class = MarcaSerializer
