#Validador de CPF

cpf = str(input('Digite o seu CPF(só os números): '))
nove_dig = cpf[:9]
multi = 10 # Variável com os valores que serão multiplicados

cpf_lista = []

for numero in nove_dig:
    num = int(numero)
    cpf_lista.append(num * multi)
    multi -= 1
calculo = (sum(cpf_lista) * 10) % 11 #Calculo para saber se o 10° está correto
result = calculo if calculo <= 9 else 0 # Se o resto da divisão for maior que 9, o valor se torna 0
dig_val = True if result == int(cpf[9]) else False

if dig_val:
    dez_dig = cpf[0:10]
    multi = 11
    cpf_lista.clear()
    for numero in dez_dig:
        num = int(numero)
        cpf_lista.append(num * multi)
        multi -= 1
    calculo = (sum(cpf_lista) * 10) % 11 #Calculo para saber se o 11° está correto
    result = calculo if calculo <= 9 else 0 # Se o resto da divisão for maior que 9, o valor se torna 0
    print(f'CPF Válido' if result == int(cpf[10]) else f'CPF Inválido')
else:
    print('CPF Inválido')

