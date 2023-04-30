#Pegando só os numeros pares de uma lista usando list comprehension (filter)

lista_a = list(range(50))

lista_b = [
    numero for numero in lista_a if numero % 2 == 0
]

print(lista_b)