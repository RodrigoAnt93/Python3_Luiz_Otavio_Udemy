#Programa para encontrar a letra que mais se repete em uma frase.

frase = input('Digite uma frase: ').lower().split()
frase = ''.join(frase)
letra = ''
rep_letra = 0

cont = 0
while cont < len(frase):
    cont_letra = frase.count(frase[cont])

    if cont_letra > rep_letra:
        rep_letra = cont_letra
        letra = frase[cont]
    cont += 1
print('')
print(f'A letra que mais se repetiu foi a letra "{letra}". Ela se repetiu {rep_letra} vezes.')