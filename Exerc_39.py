# isinstace - para sabre se objeto é determinado tipo
lista = [
    'uma', 1, 1.1, True, [0, 1, 2], (1, 2),
    {5}, {'nome': 'Rodrigo'}, 'ss', 'L2', 55, 8
]

lista_2 =[
    i for i in lista if isinstance(i, int)
]

print(lista_2)