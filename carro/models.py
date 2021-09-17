from django.db import models

from marca.models import Marca


class Carro(models.Model):
    nome = models.CharField(name='nome', max_length=100, null=False)
    km_por_galao = models.FloatField(name='km_por_galao')
    cilindros = models.SmallIntegerField(name='cilindros')
    cavalo_de_forca = models.SmallIntegerField(name='cavalo_de_forca')
    peso = models.SmallIntegerField(name='peso')
    aceleracao = models.SmallIntegerField(name='aceleracao')
    ano = models.DateField(name='ano')
    origem = models.CharField(name='origem', max_length=20)
    marca = models.ForeignKey(Marca, name='marca_id', null=False, on_delete=models.PROTECT)

    def __str__(self):
        return self.nome

    class Meta:
        db_table = 'carro'
