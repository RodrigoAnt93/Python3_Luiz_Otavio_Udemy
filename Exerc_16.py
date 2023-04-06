#Criar uma função para multiplicar numeros não nomeados

def multiplicar(*args):
    total = 1
    for num in args:
        if num > 0: #Qual número multipicado por 0 é 0.
            total *= num
    return total


print(multiplicar(5, 7, 6, 0, 0, 4))



