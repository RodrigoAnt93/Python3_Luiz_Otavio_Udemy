# Usando o @classmethod
class Pessoa:
    def __init__(self, nome, idade, sexo):
        self.nome = nome
        self.idade = idade
        self.sexo = sexo

    @classmethod
    def sem_dados(cls, sexo):
        return cls('nome desconhecido', 'idade desconhecida', sexo)


p1 = Pessoa('Rodrigo', 29, 'masculino')
p2 = Pessoa.sem_dados('feminino')
print(vars(p1))
print(vars(p2))