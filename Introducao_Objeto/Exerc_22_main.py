pokemon = [{'name': 'Bulbasaur', "atbt_base": [45, 50, 50, 65, 65, 45], 'type': ['Planta', 'Venenoso'], 'move': {1: ['Tackle', 35], 2: ['Vine Whip', 35]}},
           {"name": "Caterpie", "atbt_base": [45, 30, 35, 20, 20, 20], "type": ["Inseto"], 'move': {1: ['Tackle', 35]}}]
from Exerc_22_class import Pokemon, Battler

bulba = Pokemon(**pokemon[0], lvl=5)
caterpie = Pokemon(**pokemon[1], lvl=10)

current_battle = Battler(bulba, caterpie)

current_battle.battle()
