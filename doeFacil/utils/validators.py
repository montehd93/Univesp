from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from . import cpf_validator, cnpj_validator
import re


def validador_cpf_ou_cnpj(valor):
    valor = re.sub(r'[^0-9]', '', valor)
    if len(valor) == 11:
        cpf_validator.cpf_validator(valor)
    elif len(valor) == 14:
        cnpj_validator.cnpj_validator(valor)
    else:
        raise ValidationError(
            _('CPF/CNPJ deve ter 11 ou 14 caracteres.'),
            code='invalid_length'
        )
