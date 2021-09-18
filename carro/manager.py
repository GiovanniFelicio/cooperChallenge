from django.db.models import Manager


class CarroManager(Manager):
    def get_queryset(self):
        return super(CarroManager, self).get_queryset()

    def find_contains_nome(self, nome: str):
        return self.get_queryset().filter(nome__contains=nome)

    def find_by_origem(self, origem: str):
        return self.get_queryset().filter(origem=origem).first()