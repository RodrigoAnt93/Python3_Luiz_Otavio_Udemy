from dados.modulo import usuario
from copy import deepcopy


def analisador(funcao, *args):
    nova_lista = deepcopy(usuario)
    def interna(args, **kwargs):
        if nova_lista[args - 1]:
            if nova_lista[args - 1]['acesso']:
                resultado_funcao = funcao(*args, **kwargs)
                return resultado_funcao
            else:
                return 'Você não tem acesso a usar essa função.'
        else:
            return 'Esse ID não existe.'
    return interna


def saudacao():
    return 'Bem vindo'



usuarios = analisador(saudacao)
print(usuarios(2))