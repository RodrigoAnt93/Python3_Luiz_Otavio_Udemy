#Atualizar os valores de produtos com a função lambda

produtos = [
    ['Produto_1', 55],
    ['Produto_2', 10],
    ['Produto_3', 8],
    ['Produto_4', 23],
    ['Produto_5', 15],
    ['Produto_6', 11],
    ['Produto_7', 20],
    ['Produto_8', 33]
]

valores = list(map(lambda item: (item[1] * 0.2) + item[1], produtos))#Criando uma lista com os valores aumentados em 20%

for valor in valores:
    print(valor)