#Usando ordenação com dicionários(lambda)

times = [
    {'time': 'Flamengo', 'colocacao': 10},
    {'time':'Corinthias', 'colocacao': 2},
    {'time':'Fortaleza', 'colocacao': 1},
    {'time': 'Bahia', 'colocacao': 9},
    {'time': 'Santa Cruz', 'colocacao': 4},
    {'time': 'Cruzeiro', 'colocacao': 3},
    {'time': 'CSA', 'colocacao': 7},
    {'time': 'Vasco', 'colocacao': 5},
    {'time': 'Sergipe', 'colocacao': 8},
    {'time': 'Remo', 'colocacao': 9}
]

times.sort(key=lambda ordem: ordem["colocacao"])

for time in times:
    print(f'{time["colocacao"]}° - {time["time"]}')