import os
from banco_dados import cadastro_aluno


def cadastrar_aluno():
    global cadastro_aluno
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
    cadastro_aluno.append(aluno)
    return 'Cadastro realizado com sucesso'


def atualizar_notas():
    global cadastro_aluno
    nome_aluno = input('Nome do aluno: ')
    for aluno in cadastro_aluno:
        if aluno['nome'] == nome_aluno:
            print(f'A 1° nota é {aluno["notas"][0]} e a 2° {aluno["notas"][1]}')
            while True:
                opc = int(input('Você quer mudar qual nota? '))
                if opc == 1 or opc == 2:
                    break
                else:
                    print('Digite 1 ou 2!')
                    print()
            nova_nota = float(input('Nova nota: '))
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
            return 'Cadastro atualizado'
    return 'Aluno não encontrado'


def deletar_aluno():
    global cadastro_aluno
    nome_aluno = str(input('Nome do aluno: ')).strip().lower()
    for inx, aluno in enumerate(cadastro_aluno):
        if aluno['nome'] == nome_aluno:
            print(f'Nome: {aluno["nome"]}, Notas: 1° - {aluno["notas"][0]} / 2° - {aluno["notas"][1]}, Situação: {aluno["status"]}')
            while True:
                opc = str(input('\033[1;33mDigite [S] para confirmar a exclusão ou [N] para cancelar: \033[m')).strip().upper()
                if opc == 'S' or opc == 'N':
                    break
                else:
                    print('\033[1;30mDigite S ou N!\033[m')
            if opc == 'S':
                del cadastro_aluno[inx]
                return print('\033[1;30mO aluno foi excluido\033[m')
            else:
                return 'A exclusão foi cancelada. Nada foi alterado no cadastro!'
    return 'Aluno não encontrado.'


def procurar_aluno():
    global cadastro_aluno
    nome_aluno = str(input('Digite o nome do aluno: ')).strip().lower()
    for aluno in cadastro_aluno:
        if aluno['nome'] == nome_aluno:
            print(f'Nome: {aluno["nome"]}, Notas: 1° - {aluno["notas"][0]} / 2° - {aluno["notas"][1]}, Situação: {aluno["status"]}')
            return ''
    return 'Aluno não encontrado!'


def sistema_aluno():
    while True:
        print('**' * 5, ' Sistema de Cadastro do Aluno ', '**' * 5)
        print('O que você deseja?\n'
              '1 = Cadastrar Aluno\n'
              '2 = Atualizar Nota\n'
              '3 = Procurar Aluno\n'
              '4 = Excluir Aluno')
        while True:
            opc = int(input('Opção: '))
            if opc == 1 or opc == 2 or opc == 3 or opc == 4:
                break
            else:
                print('Digite uma opção válida!')
        escolha = {
            1: lambda: cadastrar_aluno(),
            2: lambda: atualizar_notas(),
            3: lambda: procurar_aluno(),
            4: lambda: deletar_aluno()
        }
        print('-_' * 15)
        escolha = escolha.get(opc)
        clear = lambda: os.system('cls')
        print(escolha())
        print()
        while True:
            opc = str(input('Ainda deseja utilizar o sistema? [S/N] ')).strip().upper()
            if opc == 'S' or opc == 'N':
                break
            else:
                print('\033[1;30mDigite S ou N!\033[m')
        if opc == 'N':
            return print('O programa finalizado!')
        clear()
