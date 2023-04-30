from copy import deepcopy
from dados.modulo import produtos
# copiar, classificado, produtos
# Exercícios

# Gere novos_produtos por cópia profunda (cópia profunda)
novos_produtos = deepcopy(produtos)
print(novos_produtos)

# Aumente os preços dos produtos a seguir em 10%
novos_produtos = [
    {**produto, 'preco': produto["preco"] * 1.1}
    for produto in novos_produtos
]

# Gere produtos_ordenados_por_nome por cópia profunda (cópia profunda)
produtos_ordenados_por_nome = deepcopy(produtos)

# Ordene os produtos por nome decrescente (do maior para menor)

produtos_ordenados_por_nome.sort(key=lambda p: p["nome"], reverse=True)
print(produtos_ordenados_por_nome)

# Gere produtos_ordenados_por_preco por cópia profunda (cópia profunda)

produtos_ordenados_por_preco = deepcopy(produtos)

# Ordene os produtos por preco crescente (do menor para maior)
produtos_ordenados_por_preco.sort(key=lambda p: p["preco"])
print(produtos_ordenados_por_preco)

