#Programa para analisar o maior numero passador.


def analisador(*args):
    print('=-=' * 11)
    print('Analisando os valores passados...')
    args = list(args[0])# 'args' vem como uma tupla que tem uma lista dentro. Converto ela para ser uma única lista com meus valores dentro.
    maior = 0
    for n in args:
        print(f'{n} ', end='')
        if n > maior:
            maior = n
    print(f'Foram passados {len(args)} valores no total.')
    print(f'O maior valor passado foi {maior}')


valores = []
while True:
    valores.append(int(input('Digite um valor: ')))
    while True:
        opc = str(input('Continuar? [S/N]: ')).upper()
        if opc[0] == 'S' or opc[0] == 'N':
            break
        else:
            print('Opcão errada. Tente novamente.')
    if opc[0] == 'N':
        break
analisador(valores)
