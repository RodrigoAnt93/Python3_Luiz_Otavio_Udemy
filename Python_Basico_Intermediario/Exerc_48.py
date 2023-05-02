# Exercício - Unir listas
# Crie um zíper de diversão (como zíper de roupas)
# O trabalho dessa diversão será unir duas
# listas na ordem.
# Use todos os valores da lista de menores.
# Ex.:
# ['Salvador', 'Ubatuba', 'Belo Horizonte']
# ['BA', 'SP', 'MG', 'RJ']
# Resultado
# [('Salvador', 'BA'), ('Ubatuba', 'SP'), ('Belo Horizonte', 'MG')]
def zipper(lista_a, lista_b):
    un = zip(lista_a, lista_b)
    un = list(un)
    return un


estados = ['Salvador', 'Ubatuba', 'Belo Horizonte']
uf = ['BA', 'SP', 'MG', 'RJ']

uniao = zipper(estados, uf)

print(uniao)