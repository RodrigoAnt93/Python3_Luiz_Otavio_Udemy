#Cadastrar jogador com gols e partidas feitas.

nome_jogador = str(input('Digite o nome do jogador: ')).title()
partidas = int(input(f'Quantidade de partidas que {nome_jogador} jogou? '))
cadastro = dict(nome=nome_jogador)
gols = []
for cont, part in enumerate(range(partidas)):
    gols.append(int(input(f'  Quantos gols na partida {cont+1}? ')))
cadastro['gols'] = gols
cadastro['total'] = sum(gols)
print('=-='* 20)
print(cadastro)
print('=-=' * 20)
for chave, valor in cadastro.items():
    print(f'O campo {chave} tem o valor {valor}')
print('=-=' * 20)
print(f'O jogador {nome_jogador} jogou {partidas} partidas:')
for num in range(partidas):
    print(f'   => Na partida {num+1} ele fez {cadastro["gols"][num]}gols.')