#Criando uma função decorada para limitar a chamada de outras funções.

def limite_chamada(funcao, *args):
    vezes = args[0]
    def interna(*args, **kwargs):
        nonlocal vezes
        if vezes > 0:
            vezes -= 1
            retorn = funcao(*args, **kwargs)
        else:
            retorn = 'Você já atingiu o máximo de vezes usando essa função '
        return retorn
    return interna


def soma(x,y):
    return x + y


somas = limite_chamada(soma, 2)# Passo a função que vou usar e a quantidade de vezes que ela vai ser usada.
print(somas(2, 1))# Aqui a função começou a ser usada.
print(somas(4, 4))
print(somas(5, 4))
print(somas(7, 7))