nome = str(input('Digite seu nome: '))
if len(nome) <= 4:
    print('Seu nome é pequeno...')
elif 5 <= len(nome) <= 6:
    print('Seu nome é bem normal.')
else:
    print('Poxa! Seu nome é muito grande...')