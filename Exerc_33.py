#Aumentando o preço dos meu produtos usando list comprehension (map)


produtos = [
    {'nome': 'Cuscuz', 'preco': 2.50},
    {'nome': 'Macarrão', 'preco': 5.00},
    {'nome': 'Arroz', 'preco': 7.50},
    {'nome': 'Feijão', 'preco': 10.00},
    {'nome': 'Farinha', 'preco': 3.75},
    {'nome': 'Açucar', 'preco': 4.80},
]

novo_produto = [
    {'nome': produto["nome"], 'preco': produto["preco"] * 1.5} #aplicando um aumento de 50% nos produtos
    for produto in produtos
]

print(*novo_produto, sep='\n')
