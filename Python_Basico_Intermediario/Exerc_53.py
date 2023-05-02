def menor_maior_vendas(lista_venda):
    nova_lista = [
        {**valor, 'vendas': [min(valor['vendas']), max(valor['vendas'])]} for valor in lista_venda
    ]
    return nova_lista


vendas = [
    {"vendedor": 'Paulo', 'vendas':[200.10, 111, 423.40, 362, 202.80, 110]},
    {"vendedor": 'Magida', 'vendas': [23, 55.20, 440, 30, 55.50, 21.90]},
    {"vendedor": 'Ricardo', 'vendas': [20.10, 498, 44.10, 70, 85.60, 129]},
    {"vendedor": 'Lucas', 'vendas': [300, 100, 422.10, 100.20, 426, 331]},
    {"vendedor": 'Vinicius', 'vendas': [98.50, 148, 43.70, 219, 256, 225]},
    {"vendedor": 'João', 'vendas': [338, 69.50, 311, 285.30, 446, 27]},
]

min_max_vendas = menor_maior_vendas(vendas) #Usando uma função
min_max_vendas_2 = map(lambda v: {**v, 'vendas': [min(v['vendas']), max(v['vendas'])]}, vendas) #Usando o map + lambda
print(*min_max_vendas, sep='\n')
print()
print(*min_max_vendas_2, sep='\n')
