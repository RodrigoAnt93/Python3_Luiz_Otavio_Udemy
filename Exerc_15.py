#Gerador de CPF:

from random import randint

digito_rand = ''
for r in range(9):
    digito_rand += str(randint(0, 9)) #Randomizar os 9 primeiros dígitos.

milti = 10 #Os multiplicadores do cálculo do 10° dígito
resultado_somado = 0
for numero in digito_rand:
    num = int(numero)
    resultado_somado += (num * milti)
    milti -= 1
calculo = (resultado_somado * 10) % 11
digito_rand += str(calculo) if calculo <= 9 else str(0)

multi = 11 #Os multiplicadores do cálculo do 11° dígito
resultado_somado = 0
for numero in digito_rand:
    num = int(numero)
    resultado_somado += (num * multi)
    multi -= 1
calculo = (resultado_somado * 10) % 11
digito_rand += str(calculo) if calculo <= 9 else str(0)
print(f'CPF: {digito_rand[0:3]}.{digito_rand[3:6]}.{digito_rand[6:9]}-{digito_rand[9:]}')
