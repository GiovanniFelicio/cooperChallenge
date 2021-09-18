from rest_framework import serializers
from architecture.common.enums.enum_exception_message import EnumExceptionMessage
from carro.models import Carro


class CarroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Carro
        fields = ('nome', 'km_por_galao', 'cilindros', 'cavalo_de_forca', 'peso', 'aceleracao', 'ano', 'origem', 'marca')

        extra_kwargs = {
            'nome': {
                'error_messages': {
                    'required': EnumExceptionMessage.REQUIRED_FIELD.format('Nome'),
                    'blank': EnumExceptionMessage.REQUIRED_FIELD.format('Nome')
                }
            },
            'km_por_galao': {
                'error_messages': {
                    'required': EnumExceptionMessage.REQUIRED_FIELD.format('Km por Galão'),
                    'blank': EnumExceptionMessage.REQUIRED_FIELD.format('Km por Galão')
                }
            },
            'cilindros': {
                'error_messages': {
                    'required': EnumExceptionMessage.REQUIRED_FIELD.format('Cilindros'),
                    'blank': EnumExceptionMessage.REQUIRED_FIELD.format('Cilindros')
                }
            },
            'cavalo_de_forca': {
                'error_messages': {
                    'required': EnumExceptionMessage.REQUIRED_FIELD.format('Cavalos de Força'),
                    'blank': EnumExceptionMessage.REQUIRED_FIELD.format('Cavalos de Força')
                }
            },
            'peso': {
                'error_messages': {
                    'required':EnumExceptionMessage.REQUIRED_FIELD.format('Peso'),
                    'blank': EnumExceptionMessage.REQUIRED_FIELD.format('Peso')
                }
            },
            'aceleracao': {
                'error_messages': {
                    'required': EnumExceptionMessage.REQUIRED_FIELD.format('Aceleração'),
                    'blank': EnumExceptionMessage.REQUIRED_FIELD.format('Aceleração')
                }
            },
            'ano': {
                'error_messages': {
                    'required': EnumExceptionMessage.REQUIRED_FIELD.format('Ano'),
                    'blank': EnumExceptionMessage.REQUIRED_FIELD.format('Ano')
                }
            },
            'origem': {
                'error_messages': {
                    'required': EnumExceptionMessage.REQUIRED_FIELD.format('Origem'),
                    'blank': EnumExceptionMessage.REQUIRED_FIELD.format('Origem')
                }
            },
            'marca': {
                'error_messages': {
                    'required': EnumExceptionMessage.REQUIRED_FIELD.format('Marca'),
                    'blank': EnumExceptionMessage.REQUIRED_FIELD.format('Marca')
                }
            },
        }
