from rest_framework import serializers

from carro.models import Carro


class CarroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Carro
        fields = ('nome', 'km_por_galao', 'cilindros', 'cavalo_de_forca', 'peso', 'aceleracao', 'ano', 'origem', 'marca')

        extra_kwargs = {
            'nome': {
                'error_messages': {
                    'required': '* O Campo {} é obrigatório'.format('Nome'),
                    'blank': '* O Campo {} é obrigatório'.format('Nome')
                }
            },
            'km_por_galao': {
                'error_messages': {
                    'required': '* O Campo {} é obrigatório'.format('Km por Galão'),
                    'blank': '* O Campo {} é obrigatório'.format('Km por Galão')
                }
            },
            'cilindros': {
                'error_messages': {
                    'required': '* O Campo {} é obrigatório'.format('Cilindros'),
                    'blank': '* O Campo {} é obrigatório'.format('Cilindros')
                }
            },
            'cavalo_de_forca': {
                'error_messages': {
                    'required': '* O Campo {} é obrigatório'.format('Cavalos de Força'),
                    'blank': '* O Campo {} é obrigatório'.format('Cavalos de Força')
                }
            },
            'peso': {
                'error_messages': {
                    'required': '* O Campo {} é obrigatório'.format('Peso'),
                    'blank': '* O Campo {} é obrigatório'.format('Peso')
                }
            },
            'aceleracao': {
                'error_messages': {
                    'required': '* O Campo {} é obrigatório'.format('Aceleração'),
                    'blank': '* O Campo {} é obrigatório'.format('Aceleração')
                }
            },
            'ano': {
                'error_messages': {
                    'required': '* O Campo {} é obrigatório'.format('Ano'),
                    'blank': '* O Campo {} é obrigatório'.format('Ano')
                }
            },
            'origem': {
                'error_messages': {
                    'required': '* O Campo {} é obrigatório'.format('Origem'),
                    'blank': '* O Campo {} é obrigatório'.format('Origem')
                }
            },
            'marca': {
                'error_messages': {
                    'required': '* O Campo {} é obrigatório'.format('Marca'),
                    'blank': '* O Campo {} é obrigatório'.format('Marca')
                }
            },
        }
