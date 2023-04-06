nome = str(input('Digite seu nome: ')).upper()

if len(nome) > 0:
    print(f'Seu nome é {nome}')
    print(f'Seu nome invertido é {nome[::-1]}')
    if ' ' not in nome:
        print('Seu nome não tem espaço.')
    else:
        print('Seu nome tem espaços')
    print(f'Seu nome tem {len("".join(nome.split()))} letras.')
    print(f'A última letra do seu nome é {nome[-1]}')
else:
    print('Você não digitou nada.')
print()
print('FIM!')
