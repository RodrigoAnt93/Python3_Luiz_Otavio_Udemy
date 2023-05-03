#Criando um sistema de ataque usando o polimorfismo
pokemon = [
    {'name': 'Gastly', 'moves':{1: ['Lick', 100], 2: ['Hypnosis', 60]}},
    {'name': 'Vulpix', 'moves': {1: ['Ember', 100], 2: ['Fire Spin', 70]}}
]

from abc import ABC, abstractmethod


class Pokemon(ABC):
    def __init__(self, name, moves):
        self.name = name
        self.moves = moves

    @abstractmethod
    def attack(self, choice) -> bool:
        pass


class MyPokemon(Pokemon):
    def attack(self, choice) -> bool:
        from random import randint
        luck = randint(1, 101)
        if self.moves[choice][1] >= luck:
            return True
        else:
            return False


class WildPokemon(Pokemon):
    def attack(self, choice) -> bool:
        from random import randint
        luck = randint(1, 101)
        if self.moves[choice][1] >= luck:
            return True
        else:
            return False


def attack_pokemon(pokemon: Pokemon):
    print(f'Escolha um ataque do {pokemon.name}:')
    for key, value in pokemon.moves.items():
        print(f'{key}: {value[0]}')
    choice = int(input('Escolha o numero do golpe: '))
    chance_move = pokemon.attack(choice)
    if chance_move:
        print(f'O {pokemon.name} atacou com o golpe {pokemon.moves[choice][0]}!!')
    else:
        print(f'O {pokemon.name} atacou com o golpe {pokemon.moves[choice][0]}, mas o golpe falhou...')


mypoke = MyPokemon(**pokemon[0])
wildpokemon = WildPokemon(**pokemon[1])

while True:
    attack_pokemon(mypoke)
    print()
    attack_pokemon(wildpokemon)
    print()