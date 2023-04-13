#Saber se o resultado da soma já foi somado usandao a função decorada.

def analisador_resultados(funcao, *args):
    set_de_resultados = set()
    def interna(*args, **kwargs):
        resultado_funcao = funcao(*args, **kwargs)
        if resultado_funcao not in set_de_resultados:
            set_de_resultados.add(resultado_funcao)
            return resultado_funcao
        else:
            return 'Esse resultado de soma já foi feito.'
    return interna


def soma(x, y):
    return x + y


valores_somados = analisador_resultados(soma)

print(valores_somados(2, 2))
print(valores_somados(1, 5))
print(valores_somados(2, 2))
print(valores_somados(3, 1))
print(valores_somados(4, 1))
