class Carro:
    def __init__(self, nome, cor, ano):
        self.nome = nome
        self.cor = cor
        self.ano = ano

    def apresentacao(self):
        print(f'O carro {self.nome} é da cor {self.cor} e seu ano é {self.ano}')


gol = Carro('Gol', 'Prata', 2014)
gol.apresentacao()
print(gol.nome)
print()
fiesta = Carro('Fiesta', "Bege", 2009)
fiesta.apresentacao()

nome = 'Rodrigo'
