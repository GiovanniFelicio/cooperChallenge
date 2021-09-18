from django.db import models

from carro.manager import CarroManager
from marca.models import Marca


class Carro(models.Model):
    REQUIRED_FIELDS = ['nome', 'origem', 'marca_id']

    nome = models.CharField(name='nome', max_length=100, null=False)
    km_por_galao = models.FloatField(name='km_por_galao', null=True)
    cilindros = models.SmallIntegerField(name='cilindros')
    cavalo_de_forca = models.SmallIntegerField(name='cavalo_de_forca')
    peso = models.FloatField(name='peso')
    aceleracao = models.FloatField(name='aceleracao', null=True)
    ano = models.DateField(name='ano')
    origem = models.CharField(name='origem', max_length=20)
    marca = models.ForeignKey(Marca, related_name="marca", null=False, on_delete=models.PROTECT)

    manager = CarroManager()

    def __str__(self):
        return self.nome

    class Meta:
        db_table = 'carro'
