from copy import deepcopy
# copiar, classificado, produtos
# Exercícios

produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]

# Aumente os preços dos produtos a seguir em 10%
produtos = [
    {**produto, 'preco': produto["preco"] * 1.1}
    for produto in produtos
]

# Gere novos_produtos por cópia profunda (cópia profunda)

novos_produtos = deepcopy(produtos)
print(novos_produtos)

# Ordene os produtos por nome decrescente (do maior para menor)

produtos.sort(key=lambda p: p["nome"], reverse=True)
print(produtos)

# Gere produtos_ordenados_por_nome por cópia profunda (cópia profunda)
produtos_ordenados_por_nome = deepcopy(produtos)

# Ordene os produtos por preco crescente (do menor para maior)
produtos.sort(key=lambda p: p["preco"])
print(produtos)

# Gere produtos_ordenados_por_preco por cópia profunda (cópia profunda)

produtos_ordenados_por_preco = deepcopy(produtos)