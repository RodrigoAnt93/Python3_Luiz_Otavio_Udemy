# Criando uma função para saber se o numero é par ou impar.


def par_ou_impar(x, *arg):
    if x > 0:
        print('O número é par.' if x % 2 == 0 else 'O numero é impar.')
    else:
        print('Digite um número maior que 0.')


par_ou_impar(51523658)
