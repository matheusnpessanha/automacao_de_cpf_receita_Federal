def conferir_e_padronizar_data(data_str):
    formatos_possiveis = [
        '%d/%m/%Y',  # Dia/Mês/Ano
        '%d-%m-%Y',  # Dia-Mês-Ano
        '%Y/%m/%d',  # Ano/Mês/Dia
        '%Y-%m-%d',  # Ano-Mês-Dia
        '%m/%d/%Y',  # Mês/Dia/Ano
        '%m-%d-%Y'   # Mês-Dia-Ano
    ]
    
    data = None
    
   
    for formato in formatos_possiveis:
        try:
                data = datetime.strptime(data_str, formato)
                break
        except ValueError:
                continue
    
    # Se a data não pôde ser convertida, retorna uma mensagem de erro
    if data is None:
            return "Formato de data inválido"
            
    
    # Padroniza a data para o formato desejado (Ano-Mês-Dia) com ano de 4 dígitos
    data_padronizada = data.strftime('%d%m%Y')
        
    return data_padronizada    