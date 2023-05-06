#Usando o dunder method __call__ para criar o método de ganho de exp e evolução do pokemon.
class Pokemon:
    def __init__(self, name, type, lvl):
        self.name = name
        self.type = type
        self._lvl = lvl
        self.exp = 0
        self.exp_next_lvl = 10

    def __call__(self, vl_exp):
        self.exp += vl_exp
        if self.exp >= self.exp_next_lvl:
            self._lvl += 1
            self.exp = self.exp_next_lvl - self.exp
            self.exp_next_lvl += self.exp_next_lvl / 100 * 30
            return f'{self.name} subiu de {self._lvl - 1} para {self._lvl}'
        return f'{self.name} agora tem {self.exp} pontos de experiência e precisa de {self.exp_next_lvl} ponto para passar de level.'


gastly = Pokemon('Gastly', ['Fantasma', 'Venenoso'], 2)
print(gastly(3))
print(gastly(3))
print(gastly(5))
print(gastly(6))
print(gastly(9))
print(gastly(5))