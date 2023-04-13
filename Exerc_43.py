def criar_analise(funcao, *args):
    def interna(*args, **kwargs):
        for arg in args:
            anl_str(arg)
        result = funcao(*args, **kwargs)
        return result
    return interna


def inverte_str(str):
    return str[::-1]


def anl_str(parametro):
    if not isinstance(parametro, str):
        raise TypeError('Isso não é uma str')



checar_parametro = criar_analise(inverte_str)
invertida = checar_parametro("rodrigo")
print(invertida)










