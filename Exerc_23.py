# Análise de idade para voto.


def eleitor():
    ano = int(input('Qual ano você nasceu? '))
    idade = 2023 - ano
    if idade < 16:
        print(f'Com {idade} anos: Não Vota!')
    elif idade >= 16 and idade < 18:
        print(f'Com {idade} anos: Voto Facultativo')
    elif idade >= 18 and idade < 65:
        print(f'Com {idade} anos: Obrigado a Votar')
    elif idade >= 65:
        print(f'Com {idade} anos: Voto Facultativo.')

eleitor()