#Usando ordenação com dicionários

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


def ordena(lista_times):
    return lista_times['colocacao']#Estou dizendo com qual 'chave' ele vai se basear para fazer a ordenação.


times.sort(key=ordena)#Estou mandando a definição da função e não a função executada. Por isso não são usadas as '()'

for time in times:
    print(f'{time["colocacao"]}° - {time["time"]}')