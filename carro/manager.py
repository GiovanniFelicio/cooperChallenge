from django.db.models import Manager


class CarroManager(Manager):
    def get_queryset(self):
        return super(CarroManager, self).get_queryset()