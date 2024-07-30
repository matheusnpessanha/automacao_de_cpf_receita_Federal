import re

def validar_e_padronizar_cpf(cpf):
    # Verifica se o CPF tem o formato correto
    if len(cpf) != 14 or not re.match(r'\d{3}\.\d{3}\.\d{3}-\d{2}', cpf):
        print("CPF inválido")
        return None
    
    cpf_usuario = re.sub(r'[^0-9]', '', cpf)
    entrada_e_sequencial = cpf_usuario == cpf_usuario[0] * len(cpf_usuario)
    
    # Verifica se todos os números são iguais (sequenciais)
    if entrada_e_sequencial:
        print('Você enviou dados sequenciais.')
        return None
    
    repetidos = [
        '00000000000', '11111111111', '22222222222', '33333333333',
        '44444444444', '55555555555', '66666666666', '77777777777',
        '88888888888', '99999999999'
    ]
    
    # Verifica se o CPF está na lista de CPFs repetidos
    if cpf_usuario in repetidos:
        print('CPF inválido')
        return None

    nove_digitos = cpf_usuario[:9]
    contador = 10

    resultado_digito_1 = 0
    for digitos in nove_digitos:
        resultado_digito_1 += int(digitos) * contador
        contador -= 1

    digito_1 = (resultado_digito_1 * 10) % 11
    if digito_1 == 10:
        digito_1 = 0

    dez_digitos = nove_digitos + str(digito_1)
    contador_regressivo = 11

    resultado_digito_2 = 0
    for digitos in dez_digitos:
        resultado_digito_2 += int(digitos) * contador_regressivo
        contador_regressivo -= 1

    digito_2 = (resultado_digito_2 * 10) % 11
    if digito_2 == 10:
        digito_2 = 0

    cpf_valido = f"{nove_digitos}{digito_1}{digito_2}"

    if cpf_usuario == cpf_valido:
        print(f"{cpf_usuario} é válido")
    else:
        print("CPF inválido")
        return None

    # Padroniza o CPF
    cpf_formatado = f"{cpf_valido[:3]}{cpf_valido[3:6]}{cpf_valido[6:9]}{cpf_valido[9:]}"
    return cpf_formatado

"""# Exemplo de uso
cpf_input = "123.456.789-09"
cpf_formatado = validar_e_padronizar_cpf(cpf_input)
if cpf_formatado:
    print(cpf_formatado)"""

