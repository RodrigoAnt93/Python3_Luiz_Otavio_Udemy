#Contado de segundos.
from time import sleep


def contador(start, end, step):
    if start < end:
        print(f'Contando de {start} a {end} de {step} em {step}:')
        for n in range(start, end + 1, step):
            print(f'{n} ', end='')
            sleep(0.5)
        print('FIM!')
        print('=-=' * 12)
    else:
        print(f'Contando de {start} a {end} de {step if step < 0 else -step} em {step if step < 0 else -step}:')
        for n in range(start, end - 1, step if step < 0 else -step):
            print(f'{n} ', end='')
            sleep(0.5)
        print('FIM!')
        print('=-=' * 12)


contador(1, 10, 1)
contador(0, 10, 2)
print('Agora é a sua vez de montar a contagem:')
inicio = int(input('Início: '))
fim = int(input('Fim: '))
passo = int(input('Passos: '))
contador(inicio, fim, passo)
