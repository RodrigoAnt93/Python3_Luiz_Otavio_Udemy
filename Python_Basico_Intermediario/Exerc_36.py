#Atualizando uma lista de alunos usando list comprehension (map)

alunos = [
    {'aluno': 'Pedro', 'nota': 5.7},
    {'aluno': 'Laura', 'nota': 8.0},
    {'aluno': 'João', 'nota': 7.2},
    {'aluno': 'Marcio', 'nota': 6.0},
    {'aluno': 'Rodrigo', 'nota': 5.4},
    {'aluno': 'Marcela', 'nota': 9.1},
    {'aluno': 'Douglas', 'nota': 3.0},
    {'aluno': 'Leticia', 'nota': 5.9},
    {'aluno': 'Cecilia', 'nota': 10.0},
    {'aluno': 'José', 'nota': 2},
]

aluno_status = [
    {**aluno, 'status': 'Aprovado'}
    if aluno['nota'] >= 6
    else {**aluno, 'status': 'Reprovado'}
    for aluno in alunos
]


print(*aluno_status, sep= '\n')

