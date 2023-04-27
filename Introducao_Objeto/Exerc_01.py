class Pessoa:
    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome


p1 = Pessoa('Rodrigo', 'Antonio')
print(p1.nome)
print(p1.sobrenome)