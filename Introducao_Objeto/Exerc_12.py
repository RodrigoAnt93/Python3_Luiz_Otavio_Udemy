#Crie uma classe chamada Pokemon com os seguintes atributos: nome, tipo, nivel e vida.
#Crie um property para obter o nível do Pokémon e um setter para definir o tipo.
class Pokemon:
    def __init__(self, name, type, level, hp):
        self._name = name
        self._type = type
        self._level = level
        self._hp = hp

    @property
    def level(self):
        return self._level

    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, new_type):
        self._type = new_type


new_pokemon = Pokemon('Gengar', ['Fantasma', 'Venenoso'], 55, 110)
print(new_pokemon.level)
new_pokemon.type = ['Planta']
print(vars(new_pokemon))