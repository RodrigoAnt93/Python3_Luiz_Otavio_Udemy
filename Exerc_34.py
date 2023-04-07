##Aumentando o preço dos meu produtos usando list comprehension (map) e desempacotamento

produtos = [
    {'nome': 'Cuscuz', 'preco': 2.50},
    {'nome': 'Macarrão', 'preco': 5.00},
    {'nome': 'Arroz', 'preco': 7.50},
    {'nome': 'Feijão', 'preco': 10.00},
    {'nome': 'Farinha', 'preco': 3.75},
    {'nome': 'Açucar', 'preco': 4.80},
]

novos_produtos = [
    {**produtos, 'preco': produtos["preco"] * 1.2}#aplicando um aumento de 20% nos produtos
    for produtos in produtos
]

print(*novos_produtos, sep='\n')