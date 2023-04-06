#Calculado While com Try e Except.
#OBS: Essa calculadora usou o try de uma forma não indicada. Mas, o intuito é reforçar o uso do try.

while True:
    print('_' * 5, ' CALCULADORA ', '_' * 5)
    num_1 = input('Digite o 1° numero: ')
    num_2 = input('Digite o 2° numero: ')
    num_confir = None
    try:
        num_1 = float(num_1)
        num_2 = float(num_2)
        num_confir = True
    except:
        num_confir = None
    if num_confir is None:
        print('Você digitou alguma opção inválida.')
        print('')
        continue
    print('')
    print('''Operadores:
        1 - SOMAR
        2 - SUBTRAIR
        3 - MULTIPLICAR
        4 - DIVIDIR  ''')
    while num_confir:
        opc = int(input('Digite uma opção: '))

        try:
            if opc > 0 and opc < 5:
                num_confir = None
        except:
            num_confir = True
        if num_confir is True:
            print('')
            print('Digite uma opção válida!')
    if opc == 1:
        print(f'O valor de {num_1} somado com {num_2} é igual a {num_1 + num_2}')

    elif opc == 2:
        print(f'O valor de {num_1} subtraido por {num_2} é igual a {num_1 - num_2}')

    elif opc == 3:
        print(f'O valor de {num_1} multiplicado com {num_2} é igual a {num_1 * num_2}')

    elif opc == 4:
        print(f'O valor de {num_1} dividido por {num_2} é igual a {num_1 / num_2}')
    print('')



