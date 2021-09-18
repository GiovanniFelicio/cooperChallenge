from django.db.models import Manager, Q


class MarcaManager(Manager):
    def __get_queryset(self):
        return super(MarcaManager, self).get_queryset()

    def find_all(self):
        return self.__get_queryset().all()
