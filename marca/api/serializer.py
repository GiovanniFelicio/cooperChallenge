from rest_framework import serializers
from architecture.common.enums.enum_exception_message import EnumExceptionMessage
from marca.models import Marca


class MarcaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Marca
        fields = ('nome', 'origem')

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
        }
