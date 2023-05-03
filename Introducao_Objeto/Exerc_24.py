#Crie uma classe abstrata chamada "Item" com atributos como nome e descrição.
#Implemente um método abstrato chamado "usar" que recebe um objeto "Pokemon" e modifica um de seus atributos.
#Crie pelo menos duas subclasses concretas da classe "Item" com implementações diferentes do método "usar".
from abc import ABC, abstractmethod

class Item(ABC):
    def __init__(self, name, description, amount):
        self.name = name
        self._description = description
        self.amount = amount

    @abstractmethod
    def to_use(self, pokemon):
        pass

class Pokemon:
    def __init__(self, name, atbt_base, type, lvl):
        self.name = name
        self.atbt_base = atbt_base
        self.type = type
        self.lvl = lvl

class HoldItem(Item):
    def __init__(self, name, description, amount):
        super().__init__(name, description, amount)

    def to_use(self, pokemon):
        print(f'Esse item vai {self._description} status do seu pokemon.')
        print(f'O status de DEF foi de {pokemon.atbt_base[2]} ', end='')
        pokemon.atbt_base[2] += round(pokemon.atbt_base[2] / 100 * 5)
        print(f'para {pokemon.atbt_base[2]}')


iron = HoldItem('Iron', 'aumentar em 5% da defesa no', 5)
gengar = Pokemon('Gengar', [50, 30, 35], ['Fantasma', 'Venenoso'], 45)#[HP, ATK, DEF]
iron.to_use(gengar)