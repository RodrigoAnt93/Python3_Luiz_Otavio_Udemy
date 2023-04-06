#Sortear jogadas de dados e mostrar o rank.

from random import randint
from time import sleep
from operator import itemgetter
jogadores = {}
quantidade_jgd = int(input('Será quantos jogadores? '))
print('=-=' * 15)
for quant, jog in enumerate(range(quantidade_jgd)):
    jogadores[f'Jogador_{quant+1}'] = randint(1,6)
for chave, valor in jogadores.items():
    print(f'{chave} tirou {valor} no dado.')
    sleep(1)
print('=-=' * 15)
cont = 1
ranking = dict(sorted(jogadores.items(), key=itemgetter(1), reverse=True)) #O 'itemgetter' serve para poder ordenar pelo valor da chave e o 'reverse' para em decrescente.
print('      RANKING DOS JOGADORES  ')
for chave, valor in ranking.items():
    print(f'  {cont}° foi o {chave} que tirou {valor}.')
    cont += 1