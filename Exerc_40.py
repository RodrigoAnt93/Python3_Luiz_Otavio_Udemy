#Leitor de número inteiro e real sendo tratados pelo 'try e except'.


def leia_int(txt):
    while True:
        try:
            num = int(input(f'{txt}'))
        except (ValueError, TypeError) as error:
            print(f'\033[1;31m{error.__class__.__name__}. Digite um valor INTEIRO válido.\033[m')
        except KeyboardInterrupt as error:
            print(f'\n\033[1;31m{error.__class__.__name__}. Usuário optou por finalizar o programa.\033[m')
            return 0
        else:
            return num


def leia_float(txt):
    while True:
        try:
            num = float(input(f'{txt}'))
        except (ValueError, TypeError) as error:
            print(f'\033[1;31m{error.__class__.__name__}. Digite um valor REAL válido.\033[m')
        except KeyboardInterrupt as error:
            print(f'\n\033[1;31m{error.__class__.__name__}. Usuário optou por finalizar o programa.\033[m')
        else:
            return num


num_int = leia_int('Digite um valor inteiro: ')
num_float = leia_float('Digite um valo real: ')
print('-=-' * 15)
print(f'O número Inteiro foi {num_int} e o Float foi {num_float}')