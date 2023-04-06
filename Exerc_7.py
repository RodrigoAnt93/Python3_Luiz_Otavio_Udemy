#Calculadora com While

while True:
    print('_' * 5, ' CALCULADORA ', '_' * 5)
    num_1 = float(input('Digite o primeiro número: '))
    num_2 = float(input('Digite o segundo número: '))
    print()
    print('''Operadores:
    1 - SOMAR
    2 - SUBTRAIR
    3 - MULTIPLICAR
    4 - DIVIDIR  ''')
    while True:
        opc = int(input('Digite uma opção: '))
        print('')
        if opc == 1:
            print(f'O valor de {num_1} somado com {num_2} é igual a {num_1 + num_2}')
            break
        elif opc == 2:
            print(f'O valor de {num_1} subtraido por {num_2} é igual a {num_1 - num_2}')
            break
        elif opc == 3:
            print(f'O valor de {num_1} multiplicado com {num_2} é igual a {num_1 * num_2}')
            break
        elif opc == 4:
            print(f'O valor de {num_1} dividido por {num_2} é igual a {num_1 / num_2}')
            break
        else:
            print('Opção inválida!')
    print('')


