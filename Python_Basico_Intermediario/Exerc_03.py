while True:
    hora = str(input('Digite a hora[hh:mm]: '))
    if hora[0:2].isnumeric():
        hora = int(hora[0:2])
        if 0 <= hora <= 11:
            print('\033[1;32mTenha um bom dia!\033[m')
        elif 11 < hora <=17:
            print('\033[1;33mTenha uma boa tarde!\033[m')
        elif 17 < hora <= 23:
            print('\033[1;34mTenha uma boa noite!\033[m')
        else:
            print('\033[1;31mERRO! Hora inválida.\033[m')
    else:
        print('\033[1;31mERRO! Hora inválida.\033[m')