from marca.models import Marca


class MarcaService(object):
    def __get_queryset(self):
        return Marca.manager