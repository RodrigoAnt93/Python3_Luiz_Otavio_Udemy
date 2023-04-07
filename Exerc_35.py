#Pegando só os produtos acima de 4,99 e aplicando o imposto usando list comprehension(map e filter)

produtos = [
    {'nome': 'Cuscuz', 'preco': 2.50},
    {'nome': 'Macarrão', 'preco': 5.00},
    {'nome': 'Arroz', 'preco': 7.50},
    {'nome': 'Feijão', 'preco': 10.00},
    {'nome': 'Farinha', 'preco': 3.75},
    {'nome': 'Açucar', 'preco': 4.80},
    ]

novo_produto = [
    {**produto, 'preco': produto["preco"] * 1.1}
    for produto in produtos if produto["preco"] > 4.99
]

print(*novo_produto, sep='\n')