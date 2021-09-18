from rest_framework import serializers
from .serializer_details import extra_kwargs
from marca.models import Marca


class MarcaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Marca
        fields = ('id', 'nome', 'origem')
        read_only_fields = ('id', )

        extra_kwargs = extra_kwargs
