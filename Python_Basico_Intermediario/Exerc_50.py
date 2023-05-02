from itertools import groupby

pokemon = [
    {1: 'Bulbasaur', "atbt_base": [45, 50, 50, 65, 65, 45], 'type': ['Planta', 'Venenoso']},
    {2: 'Ivysaur', 'atbt_base': [60, 62, 63, 80, 80, 60], 'type': ['Planta', 'Venenoso']},
    {3: 'Venusaur', 'atbt_base': [85, 85, 85, 100, 100, 80], 'type': ['Planta', 'Venenoso']},
    {4: 'Charmander', 'atbt_base': [45, 55, 45, 60, 50, 65], 'type': ['Fogo']},
    {5: 'Charmeleon', 'atbt_base': [58, 64, 58, 80, 65, 80], 'type': ['Fogo']},
    {6: 'Charizard', 'atbt_base': [78, 84, 78, 110, 85, 100], 'type': ['Fogo', 'Voador']},
    {7: 'Squirtle', 'atbt_base': [49, 48, 65, 50, 65, 43], 'type': ['Água']},
    {8: 'Wartortle', 'atbt_base': [64, 63, 80, 65, 75, 58], 'type': ['Água']},
    {9: 'Blastoise', 'atbt_base': [85, 85, 100, 85, 100, 80], 'type': ['Água']}
    ]

typ_pokemon = groupby(pokemon, key= lambda t: t['type'])

for key, values in typ_pokemon:
    print(key)
    for poke in values:
        print(poke)
    print()