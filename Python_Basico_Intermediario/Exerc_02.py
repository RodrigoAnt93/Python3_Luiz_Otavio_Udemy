
while True:
    num = input('Digite um número: ')
    if num.isnumeric():
        num = int(num)
        if num % 2 == 0:
            print(f'Você digitou {num} e ele é \033[1;34mPAR\033[m')
        else:
            print(f'Você digitou {num} e ele é \033[1;33mIMPAR\033[m')
    else:
        print('\033[1;31mDigite um valor inteiro!\033[m')