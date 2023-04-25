

while True:
    nome = str(input('Digite seu nome: ')).upper()
    cont = 0
    while cont < len(nome):
        print(nome[cont])
        cont += 1
    print()