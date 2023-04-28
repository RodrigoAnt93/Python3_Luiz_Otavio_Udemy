#Criar uma função para calcular o metro quadrado de uma área.

def cal_metros(larg, comp):
    return larg * comp


print(' Controle de terreno')
print('=-' * 10)
largura = float(input('LARGURA: '))
comprimento = float(input('COMPRIMENTO: '))
print('')
print(f'A área de um terreno {largura:.2f}x{comprimento:.2f} é {cal_metros(largura, comprimento):.2f}m²')