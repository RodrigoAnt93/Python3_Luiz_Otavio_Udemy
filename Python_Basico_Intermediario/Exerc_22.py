#Sorteando numeros e somando só os pares

from random import randint
from time import sleep


def sorteio():
    def par(lista):
        val_par = 0
        for v in lista:
            if v % 2 == 0:
                val_par += v
        print(f'Somando os valores pares de {lista}, temos {val_par}')


    valores = []
    for v in range(5):
        valores.append(randint(0, 10))
    print('Sorteando 5 valores da lista: ', end='')
    for v in valores:
        sleep(0.5)
        print(f'{v} ', end='')
    print('PRONTO!')
    sleep(1)
    par(valores)



sorteio()