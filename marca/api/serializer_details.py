from architecture.common.enums.enum_exception_message import EnumExceptionMessage

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
