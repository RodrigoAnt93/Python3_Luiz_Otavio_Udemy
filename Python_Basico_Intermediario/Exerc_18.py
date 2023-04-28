#Criando uma função com multiplicadores usando o Closure


def criar_multiplicador(multiplo):# Aqui vamos receber o numero multiplicador.
    def multiplicador(numero): #Aqui criaremos o Closure que vai receber o numera a ser multiplicado.
        return numero * multiplo
    return multiplicador

dobrar = criar_multiplicador(2) #Aqui enviamos só um valor que será o multiplo da função 'criar_multiplicador'.
triplicar = criar_multiplicador(3)
quadruplicar = criar_multiplicador(4)

print(dobrar(2)) #Aqui entregamos o valor da função closure 'multiplicador' e assim finalizando sua execução.
print(triplicar(2))
print(quadruplicar(2))
