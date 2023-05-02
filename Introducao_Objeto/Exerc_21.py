#Crie uma classe abstrata chamada "Pokemon" com um método abstrato "atacar".
#Crie pelo menos duas subclasses concretas da classe "Pokemon" com implementações diferentes do método "atacar".
from abc import ABC, abstractmethod


class Pokemon(ABC):
    def __init__(self, name, type):
        self.name = name
        self.type = type

    @abstractmethod
    def _attack(self, msg):
        ...

    def direct_attack(self, damage):
        self._attack(f'Ataque direto: {self.name} tirou {damage} de dano no ataque')


class WildPokemon(Pokemon):
    def __init__(self,name, type, lvl):
        super().__init__(name, type)
        self.lvl = lvl

    def _attack(self, msg):
        print(f'Pokemon selvagem: {msg}')


class YouPokemon(Pokemon):
    def __init__(self,name, type, lvl):
        super().__init__(name, type)
        self.lvl = lvl

    def _attack(self, msg):
        print(f'Seu Pokemon: {msg}')


gastly = WildPokemon('Gastly', ['Fantasma', 'Venenoso'], 25)
cubone = YouPokemon('Cubone', ['Terra'], 19)

gastly.direct_attack(22)
cubone.direct_attack(17)
