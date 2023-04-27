import os

lista = []

while True:
    opc = str(input('Digite uma opção:\n'
                    '[I]nserir - [A]pagar - [L]istar: ')).upper()
    if opc == 'I':
        lista.append(input('Digite o que você quer inserir: '))
        print('Foi inserido com sucesso!')
        print('')
    elif opc == 'A':
        if len(lista) == 0:
            print('Lista vazia!')
            print('')
        else:
            for ind, item in enumerate(lista):
                print(f'{ind} = {item}')
            lista.pop(int(input('Digite o índice do item que quer excluir: ')))
            print('Item excluido com sucesso!')
    elif opc == 'L':
        if len(lista) == 0:
            print('Lista vazia!')
            print('')
        else:
            for ind, item in enumerate(lista):
                print(f'{ind} = {item}')
            print('')
    else:
        print('Por favor digitar as opções I, A ou L.')
