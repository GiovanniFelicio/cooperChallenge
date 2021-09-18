from carro.models import Carro


class CarroService(object):
    def __get_queryset(self):
        return Carro.manager
