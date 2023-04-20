# Criando condicionais sem os "IF's"

def somar(x, y):
    return x + y
def subtrair(x, y):
    return  x - y
def multiplicar(x, y):
    return x * y
def dividir(x, y):
    return x / y
def zerar():
    return 'Operação cancelada\n'

while True:
    valor_1 = float(input('Digite um valor: '))
    valor_2 = float(input('Digite outro valor: '))
    print('')
    print('Somar \n'
            'Subtrair \n'
            'Multiplicar \n'
            'Dividir\n'
            'Zerar\n'
            'Sair')
    opc = str(input('Digite uma opção: ')).lower()
    comandos = {
        'somar': lambda: somar(valor_1, valor_2),
        'subtrair': lambda: subtrair(valor_1, valor_2),
        'multiplicar': lambda: multiplicar(valor_1, valor_2),
        'dividir': lambda: dividir(valor_1, valor_2),
        'zerar': lambda: zerar()
    }
    if opc == 'sair':
        break
    else:
        comando = comandos.get(opc)
    print(comando())
