#Criando uma tabela de campeonato já ordenada com empacotamento na função.


def criar_tabela(*kwargs):
    time = list(kwargs)
    time.sort(key=lambda p: p["pontos"], reverse=True)
    print('')
    for num, clube in enumerate(time):
        print(f'{num+1}° - {clube["nome"]:<15} {clube["pontos"]:>5}')


times = []
while True:
    times.append(dict(nome=input('Time: ').title(), pontos=int(input('Pontos: '))))
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
