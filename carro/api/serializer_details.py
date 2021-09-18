from architecture.common.enums.enum_exception_message import EnumExceptionMessage

extra_kwargs = {
    'nome': {
        'error_messages': {
            'required': EnumExceptionMessage.REQUIRED_FIELD.value.format('Nome'),
            'blank': EnumExceptionMessage.REQUIRED_FIELD.value.format('Nome')
        }
    },
    'km_por_galao': {'write_only': True, 'required': False, },
    'cilindros': {
        'write_only': True,
        'error_messages': {
            'required': EnumExceptionMessage.REQUIRED_FIELD.value.format('Cilindros'),
            'blank': EnumExceptionMessage.REQUIRED_FIELD.value.format('Cilindros')
        }
    },
    'cavalo_de_forca': {
        'write_only': True,
        'error_messages': {
            'required': EnumExceptionMessage.REQUIRED_FIELD.value.format('Cavalos de força'),
            'blank': EnumExceptionMessage.REQUIRED_FIELD.value.format('Cavalos de força')
        }
    },
    'peso': {
        'write_only': True,
        'error_messages': {
            'required': EnumExceptionMessage.REQUIRED_FIELD.value.format('Peso'),
            'blank': EnumExceptionMessage.REQUIRED_FIELD.value.format('Peso')
        }
    },
    'aceleracao': {'write_only': True, 'required': False},
    'origem': {
        'error_messages': {
            'required': EnumExceptionMessage.REQUIRED_FIELD.value.format('Origem'),
            'blank': EnumExceptionMessage.REQUIRED_FIELD.value.format('Origem')
        }
    },
    'ano': {
        'write_only': True,
        'error_messages': {
            'required': EnumExceptionMessage.REQUIRED_FIELD.value.format('Ano'),
            'blank': EnumExceptionMessage.REQUIRED_FIELD.value.format('Ano')
        }
    },
    'marca_id': {
        'write_only': True,
        'error_messages': {
            'required': EnumExceptionMessage.REQUIRED_FIELD.value.format('Marca'),
            'blank': EnumExceptionMessage.REQUIRED_FIELD.value.format('Marca')
        }
    }
}