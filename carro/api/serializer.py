from rest_framework import serializers

from marca.api.serializer import MarcaSerializer
from .serializer_details import extra_kwargs
from carro.models import Carro


class CarroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Carro
        fields = ('id', 'nome', 'km_por_galao', 'cilindros', 'cavalo_de_forca', 'peso', 'aceleracao', 'origem', 'ano', 'marca')
        read_only_fields = ('id',)

        extra_kwargs = extra_kwargs


class CarroDetailSerializer(serializers.ModelSerializer):

    marca = MarcaSerializer()

    class Meta:
        model = Carro
        fields = ('id', 'nome', 'km_por_galao', 'cilindros', 'cavalo_de_forca', 'peso', 'aceleracao', 'origem', 'ano', 'marca')
        read_only_fields = ('id', 'nome', 'km_por_galao', 'cilindros', 'cavalo_de_forca', 'peso', 'aceleracao', 'origem', 'ano', 'marca')