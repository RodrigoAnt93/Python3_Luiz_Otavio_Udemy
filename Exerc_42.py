# Exercício - Adiando a execução de funções
def soma(x, y):
    return x + y


def multiplica(x, y):
    return x * y


def criar_funcao(funcao, *args):
    x = args[0]
    def interna(args):
        return funcao(x, args)
    return interna

soma_com_cinco = criar_funcao(soma, 5)
multiplica_por_dez = criar_funcao(multiplica, 10)

print(soma_com_cinco(7))
print(multiplica_por_dez(10))