from marca.models import Marca


class MarcaService(object):
    def __get_queryset(self):
        return Marca.manager

    def find_contains_nome(self, nome: str) -> [Marca]:
        return self.__get_queryset().find_contains_nome(nome)

    def find_by_origem(self, origem: str) -> Marca:
        return self.__get_queryset().find_by_origem(origem)
