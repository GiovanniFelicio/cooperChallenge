from carro.models import Carro


class CarroService(object):
    def __get_queryset(self):
        return Carro.manager

    def find_contains_nome(self, nome: str) -> [Carro]:
        return self.__get_queryset().find_contains_nome(nome)

    def find_by_origem(self, origem: str) -> Carro:
        return self.__get_queryset().find_by_origem(origem)
