from func_data import conferir_e_padronizar_data
from func_cpf import validar_e_padronizar_cpf
import json


arquivo = [{'cpf': '116.779.734-55', 'data': '30/11/1996'}, {'cpf': '123.456.789-00', 'data': '01/01/2000'}]

'''for usuario in arquivo:
    data.conferir_e_padronizar_data(usuario)'''


arquivo = [
        {'cpf': '116.779.734-55', 'data': '30/11/1996'},
        {'cpf': '123.456.789-00', 'data': '01/01/2000'},
        {'cpf': '123.456.789-09', 'data': '04/04/2007'},
        {'cpf': '514.218.794-68', 'data': '09/78/2023'}
    ]
    
resultados = []
    
for usuario in arquivo:
    cpf_validado = validar_e_padronizar_cpf(usuario['cpf'])
    data_padronizada = conferir_e_padronizar_data(usuario['data'])
    if cpf_validado and data_padronizada != "Formato de data inválido":
        resultados.append({
            'cpf': cpf_validado,
            'data': data_padronizada
        })
    else:
        print(f"Erro ao validar: {usuario}")

with open('teste_funcao.json', 'w', encoding='utf-8') as file:
    json.dump(resultados, file, ensure_ascii=False, indent=4)

print("Resultados salvos em teste_funcao.json")