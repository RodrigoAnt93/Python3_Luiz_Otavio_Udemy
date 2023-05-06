#Decoradores com Class.
class MyReprMixin:
    def __repr__(self):
        class_name = type(self).__name__
        class_dict = self.__dict__
        class_repr = f'{class_name}({class_dict})'
        return class_repr


class Pokemon:
    def __init__(self, name, type, lvl):
        self.name = name
        self.type = type
        self._lvl = lvl

    def attack(self):
        return f'{self.name} começou a atacar!'


class WildPokemon(Pokemon, MyReprMixin):
    pass


class MyPokemon(Pokemon, MyReprMixin):
    pass


gengar = MyPokemon('Gengar', ['Fantasma', 'Venenoso'], 45)
marowak = WildPokemon('Marowak', ['Terra'], 34)
print(gengar)
print(marowak)
print(gengar.attack())
print(marowak.attack())