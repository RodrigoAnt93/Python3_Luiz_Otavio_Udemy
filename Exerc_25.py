#Cadastro com condicional em dicionário

nome = str(input('Nome Aluno: ')).title()
media = float(input('Média: '))
alunos= dict(nome=nome, media=media, situação='aprovado' if media>=7 else 'reprovado')
print('=-=' * 20)
for chaves, valor in alunos.items():
    print(f'{chaves} é igual a {valor}')

