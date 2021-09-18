from rest_framework import serializers
from architecture.common.enums.enum_exception_message import EnumExceptionMessage
from carro.models import Carro


class CarroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Carro
        fields = ('nome', 'origem', 'ano')

        extra_kwargs = {
            'nome': {
                'error_messages': {
                    'required': EnumExceptionMessage.REQUIRED_FIELD.value.format('Nome'),
                    'blank': EnumExceptionMessage.REQUIRED_FIELD.value.format('Nome')
                }
            },
            'origem': {
                'error_messages': {
                    'required': EnumExceptionMessage.REQUIRED_FIELD.value.format('Origem'),
                    'blank': EnumExceptionMessage.REQUIRED_FIELD.value.format('Origem')
                }
            },
            'ano': {
                'error_messages': {
                    'required': EnumExceptionMessage.REQUIRED_FIELD.value.format('Ano'),
                    'blank': EnumExceptionMessage.REQUIRED_FIELD.value.format('Ano')
                }
            }
        }
