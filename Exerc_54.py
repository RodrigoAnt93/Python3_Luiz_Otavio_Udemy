def decodificador(lista_senha):
    senha_decodificada = []
    vlr_0 = 0
    vlr_1 = 0
    for idx, linha in enumerate(lista_senha):
        for i, l in enumerate(linha):
            if lista_senha[i][idx] == '0':
                vlr_0 += 1
            else:
                vlr_1 += 1
        if vlr_1 >= vlr_0:
            senha_decodificada.append(1)
        else:
            senha_decodificada.append(0)
        vlr_0 = 0
        vlr_1 = 0
    return senha_decodificada


senha = [
'0110100000',
'1001011111',
'1110001010',
'0111010101',
'0011100110',
'1010011001',
'1101100100',
'1011010100',
'1001100111',
'1000011000'
]

senha_descodificada = decodificador(senha)

print(senha_descodificada)