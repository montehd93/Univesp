from django.core.exceptions import ValidationError


def cnpj_validator(cnpj):
    if len(cnpj) != 14:
        raise ValidationError('CNPJ inválido')

    soma = 0
    for i in range(12):
        soma += int(cnpj[i]) * ((4 - i) % 8 + 2)
    resto = soma % 11
    if resto < 2:
        digito1 = 0
    else:
        digito1 = 11 - resto

    soma = 0
    for i in range(13):
        soma += int(cnpj[i]) * ((3 - i) % 8 + 2)
    resto = soma % 11
    if resto < 2:
        digito2 = 0
    else:
        digito2 = 11 - resto

    if digito1 != int(cnpj[12]) or digito2 != int(cnpj[13]):
        raise ValidationError('CNPJ inválido')
