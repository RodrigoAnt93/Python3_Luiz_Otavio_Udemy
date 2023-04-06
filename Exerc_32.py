#Criando uma tabela de campeonato já ordenada com empacotamento na função.


def criar_tabela(*kwargs):
    print(kwargs)




times = []
while True:
    times.append(dict(nome=input('Time: ').title(), pontos=input('Pontos: ')))
    print('')
    while True:
        opc = input('Continuar? [S/N] ').upper()[0]
        if opc in 'SN':
            break
        else:
            print('Opção inválida!')
    if opc == 'N':
        break

print(criar_tabela(*times))
