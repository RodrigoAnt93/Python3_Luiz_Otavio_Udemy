#Validador o 10° dígito do CPF.

cpf = str(input('Digite o seu CPF(só os números): '))
multi = 10 # Variável com os valores que serão mutiplicados

cpf_lista = []

for numero in cpf:
    if multi < 2: # If para quebrar as multiplicações quando chegar no 9° dígito do CPF
        break
    num = int(numero)
    cpf_lista.append(num * multi)
    multi -= 1
calculo = (sum(cpf_lista) * 10) % 11 #Calculo para saber se o 10° está correto
result = calculo if calculo <= 9 else 0 # Se o resto da divisão for maior que 9, o valor se torna 0
print(f'CPF Válido' if result == int(cpf[9]) else f'CPF Inválido')
