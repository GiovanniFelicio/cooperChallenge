from django.db.models import Manager, Q


class MarcaManager(Manager):
    def __get_queryset(self):
        return super(MarcaManager, self).get_queryset()

    def find_all(self):
        return self.__get_queryset().all()

    def find_contains_nome(self, nome: str):
        return self.__get_queryset().filter(nome__contains=nome)

    def find_by_origem(self, origem: str):
        return self.__get_queryset().filter(origem=origem).first()

    def find_by_origem_and_contains_nome(self, origem: str, nome: str):
        return self.__get_queryset().filter(origem=origem, nome__contains=nome)
