#Função decoradora com Class.
def my_repr_mixin(cls):
    def my_repr(self):
        class_name = self.__class__.__name__
        class_dict = self.__dict__
        class_repr = f'{class_name}({class_dict})'
        return class_repr
    cls.__repr__ = my_repr
    return cls


@my_repr_mixin
class Pokemon:
    def __init__(self, name, type, lvl):
        self.name = name
        self.type = type
        self._lvl = lvl

    def attack(self):
        return f'{self.name} começou a atacar!'


class WildPokemon(Pokemon):
    pass


class MyPokemon(Pokemon):
    pass


gengar = MyPokemon('Gengar', ['Fantasma', 'Venenoso'], 45)
marowak = WildPokemon('Marowak', ['Terra'], 34)
print(gengar)
print(marowak)
print(gengar.attack())
print(marowak.attack())