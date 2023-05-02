def analisador(numero, num_analisar):
    num_analisar = str(num_analisar)
    numero = str(numero)
    cont = -1
    for n in num_analisar:
        if numero.index(n) > cont:
            cont = int(numero.index(n))
        else:
            return False
    return True


print(analisador(12345, 13))

