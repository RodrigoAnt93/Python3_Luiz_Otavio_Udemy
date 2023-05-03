#Crie uma classe abstrata chamada "Treinador" com atributos como nome, idade, cidade e uma referência à Pokedex do treinador.
#Implemente um método abstrato chamado "capturar_pokemon" que recebe um objeto "Pokemon" e adiciona-o à Pokedex do treinador.
#Crie pelo menos duas subclasses concretas da classe "Treinador" com implementações diferentes do método "capturar_pokemon".
from abc import ABC, abstractmethod
class Pokedex:
    def __init__(self):
        self._pokedex = []
        self.ensign = []
    @property
    def pokedex(self):
        return self._pokedex
class Pokemon:
    def __init__(self, name, type, lvl):
        self.name = name
        self.type = type
        self.lvl = lvl

class Treiner(ABC):
    def __init__(self, name, age, city):
        self._name = name
        self._age = age
        self._city = city
        self.pokedex = Pokedex()

    @abstractmethod
    def catch_pokemon(self, new_pokemon):
        pass

class NewTreiner(Treiner):
    def __init__(self, name, age, city):
        super().__init__(name, age, city)
        self.list_pokemon = []

    def catch_pokemon(self, new_pokemon):
        self.list_pokemon.append(new_pokemon)
        self.pokedex._pokedex.append(vars(new_pokemon))


treiner = NewTreiner('Rodrigo', 29, 'Pallet')
gengar = Pokemon('Gengar', ['Fantasma', 'Venenoso'], 45)
treiner.catch_pokemon(gengar)
print(treiner.pokedex.pokedex)
print(treiner.list_pokemon[0].name)