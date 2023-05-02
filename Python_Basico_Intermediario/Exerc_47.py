def analisador_type(funcao, tipo, *args):
    type = tipo

    def interna(*args, **kwargs):
        for arg in args:
            is_type(type, arg)
        resultado =  funcao(*args, **kwargs)
        return resultado
    return interna


def is_type(tipo, parametro):
    if not isinstance(parametro, tipo):
        raise TypeError('Esse valor não é do tipo correto.')


def soma(x, y):
    return x + y



soma_analisado = analisador_type(soma, int)
print(soma_analisado(5, 5))
print(soma_analisado(2, 2))
print(soma_analisado('5', 1))