# Criando condicionais sem os "IF's"
from copy import deepcopy
cadastro_aluno = []


def cadastrar_aluno(*args):
    aluno = dict()
    aluno['nome'] = input('Nome: ').lower().strip()
    notas = []
    notas.append(float(input('1° nota: ')))
    notas.append(float(input('2° nota: ')))
    aluno['notas'] = notas
    if sum(aluno['notas']) / 2 >= 6:
        aluno['status'] = 'Aprovado'
    else:
        aluno['status'] = 'Reprovado'
    return aluno


def atualizar_notas(list_aluno):
    global cadastro_aluno
    nome_aluno = input('Nome do aluno: ')
    lista_aluno = deepcopy(list_aluno)
    for aluno in lista_aluno:
        if aluno['nome'] == nome_aluno:
            cadastro_aluno.clear()
            print(f'A 1° nota é {aluno["notas"][0]} e a 2° {aluno["notas"][1]}')
            while True:
                opc = int(input('Você quer mudar qual nota? '))
                if opc == 1 or opc == 2:
                    break
                else:
                    print('Digite 1 ou 2!')
                    print()
            nova_nota = int(input('Nova nota: '))
            if opc == 1:
                aluno['notas'].pop(0)
                aluno['notas'].insert(0, nova_nota)
            else:
                aluno['notas'].pop()
                aluno['notas'].append(nova_nota)
            if sum(aluno['notas']) / 2 >= 6:
                aluno['status'] = 'Aprovado'
            else:
                aluno['status'] = 'Reprovado'
            return lista_aluno
    return 'Aluno não encontrado'


cadastro_aluno.append(cadastrar_aluno())
print()
print(cadastro_aluno)
cadastro_aluno.append(atualizar_notas(cadastro_aluno))
print(cadastro_aluno)
