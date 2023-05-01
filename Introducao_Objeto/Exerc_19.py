from random import randint
gastly = {'name': 'Gengar', 'type': ['Fantasma', 'Venenoso'], 'lvl': 35, 'total_hp': 100, 'catch_rate': 45}
class Pokeball:
    def __init__(self, type, chance, amount):
        self.type = type
        self.chance = chance
        self.amount = amount

    def capture(self, battle_result):
        catch_percentage = randint(1, 100)
        self.battle_result = battle_result
        chance = round(((((3 * self.battle_result.wild_pokemon.total_hp - 2 * self.battle_result.current_hp)
                   * (self.battle_result.wild_pokemon.catch_rate * self.chance)) / (3 * self.battle_result.wild_pokemon.total_hp)) * self.battle_result.status) / 10, 2)

        if chance >= catch_percentage:
            self.amount -= 1
            print(f'Você teve {chance}% de chance para capturar o {self.battle_result.wild_pokemon.name} e conseguiu. PARABÉNS!')
            return [True, self.battle_result.wild_pokemon]
        else:
            self.amount -= 1
            print(f'Você teve {chance}% de chance para capturar o {self.battle_result.wild_pokemon.name} e a pokebola quebrou. Lamento...')
            return [False]

class Treiner:
    def __init__(self, name, age, city):
        self.name = name
        self.age = age
        self.city = city
        self.list_pokemon = []
        self.warehouse = []

    def new_pokemon(self, new_pokemon):
        if new_pokemon[0]:
            if len(self.list_pokemon) <= 6:
                self.list_pokemon.append(new_pokemon[1])
            else:
                self.warehouse.append(new_pokemon[1])

    def list_poke(self):
        if len(self.list_pokemon) != 0:
            for ind, pokemon in enumerate(self.list_pokemon):
                print(f'{ind+1} - {pokemon.name}')
        else:
            return 'Você não tem pokemon'

class Battle_Pokemon():

    def __init__(self, current_hp, status):
        self.current_hp = current_hp
        self.status = status

class Pokemon:
    def __init__(self, name, type, lvl, total_hp, catch_rate):
        self.name = name
        self.type = type
        self.lvl = lvl
        self.total_hp = total_hp
        self.catch_rate = catch_rate

class Wild_Pokemon(Battle_Pokemon):
    def __init__(self, pokemon):
        self.wild_pokemon = Pokemon(**pokemon)
        Battle_Pokemon.__init__(self, current_hp=self.wild_pokemon.total_hp, status=None)


treiner = Treiner('Rodrigo', 29, 'Pallet')
great_ball = Pokeball(type='Great Ball', chance=1.5, amount=10)
while True:
    print('Um pokemon selvagem foi encontrado!')
    current_battle = Wild_Pokemon(gastly)
    print(f'{current_battle.wild_pokemon.name} sofreu um dano de 20')
    current_battle.current_hp -= 20
    print(f'{current_battle.wild_pokemon.name} foi queimado!')
    current_battle.status = 6
    print(f'{current_battle.wild_pokemon.name} sofreu um dano de 50')
    current_battle.current_hp -= 50
    print(treiner.new_pokemon(great_ball.capture(current_battle)))
    print(treiner.list_poke())
    stop = input('continuar?')