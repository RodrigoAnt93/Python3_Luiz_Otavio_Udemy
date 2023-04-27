import json
dict_class_poke = [
    {'name': 'Bulbasaur', 'type': ['Grass', 'Poison']},
    {'name': 'Squirtle', 'type': ['Water']},
    {'name': 'Charmander', 'type': ['Fire']}
]

with open('class_pokemon.json', 'w', encoding='utf8') as pokemon:
    json.dump(dict_class_poke, pokemon, indent=2, ensure_ascii=False)