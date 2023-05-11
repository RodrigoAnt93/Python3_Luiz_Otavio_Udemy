#Classes decoradoras.
class Multiplicar:
    def __init__(self, func):
        self.func = func
        self.multiplicador = 10

    def __call__(self, *args, **kwargs):
        resultado = self.func(*args, **kwargs)
        return resultado * self.multiplicador


@Multiplicar
def soma(x, y):
    return x + y


somar = soma(5, 5)
print(somar)