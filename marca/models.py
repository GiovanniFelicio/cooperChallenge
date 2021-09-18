from django.db import models

from marca.manager import MarcaManager


class Marca(models.Model):

    nome = models.CharField(max_length=100)
    origem = models.CharField(max_length=20)

    manager = MarcaManager()

    def __str__(self):
        return self.nome

    class Meta:
        db_table = 'marca'