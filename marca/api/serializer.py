from rest_framework import serializers
from marca.models import Marca


class MarcaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Marca
        fields = ('nome', 'origem')

        extra_kwargs = {
            'nome': {
                'error_messages': {
                    'required': '* O Campo {} é obrigatório'.format('Nome'),
                    'blank': '* O Campo {} é obrigatório'.format('Nome')
                }
            },
            'origem': {
                'error_messages': {
                    'required': '* O Campo {} é obrigatório'.format('Origem'),
                    'blank': '* O Campo {} é obrigatório'.format('Origem')
                }
            },
        }
