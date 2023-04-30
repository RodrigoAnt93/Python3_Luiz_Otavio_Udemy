#Crie uma classe chamada Pokebola com os seguintes atributos: tipo, chance_captura e quantidade.
#Crie um método chamado capturar que recebe como argumento um objeto da classe Pokemon e retorna um valor booleano que indica
#se a captura foi bem-sucedida ou não, com base na chance de captura do Pokémon.
'''Catch Rate = (((3 * Max HP - 2 * HP) * (Catch Rate * Ball Modifier)) / (3 * Max HP)) * Status Modifier

Onde:

Max HP é o máximo de pontos de vida do Pokémon;
HP é o atual número de pontos de vida do Pokémon;
Catch Rate é a taxa base de captura do Pokémon;
Ball Modifier é o bônus de captura da Pokébola utilizada (1 para a Pokébola, 1.5 para a Great Ball, 2 para a Ultra Ball e 0.1 para a Safari Ball);
Status Modifier é o modificador de status (1 para status normal, 1.5 para envenenado ou queimado e 2 para congelado, paralisado ou dormindo).'''
from random import randint


class Pokemon:
    def __init__(self, name, total_hp, catch_rate):
        self.name = name
        self.total_hp = total_hp
        self.catch_rate = catch_rate


class Battle_Pokemon():

    def __init__(self, current_hp, status, pokemon_obj):
        self.current_hp = current_hp
        self.status = status
        self.pokemon_obj = pokemon_obj


class Pokeball:
    def __init__(self, type, chance, amount):
        self.type = type
        self.chance = chance
        self.amount = amount

    def capture(self, battle_result):
        catch_percentage = randint(1, 100)
        self.battle_result = battle_result
        chance = round(((((3 * self.battle_result.pokemon_obj.total_hp - 2 * self.battle_result.current_hp)
                   * (self.battle_result.pokemon_obj.catch_rate * self.chance)) / (3 * self.battle_result.pokemon_obj.total_hp)) * self.battle_result.status) / 10, 2)

        if chance >= catch_percentage:
            self.amount -= 1
            return f'Você teve {chance}% de chance para capturar o {self.battle_result.pokemon_obj.name} e conseguiu. PARABÉNS!'
        else:
            self.amount -= 1
            return f'Você teve {chance}% de chance para capturar o {self.battle_result.pokemon_obj.name} e a pokebola quebrou. Lamento...'


gastly = Pokemon(name='Gastly', total_hp=60, catch_rate=190)
current_battle = Battle_Pokemon(current_hp=30, status=1.5, pokemon_obj=gastly)# 50% do HP e queimado.
great_ball = Pokeball(type='Great Ball', chance=1.5, amount=10)
print(great_ball.capture(current_battle))
