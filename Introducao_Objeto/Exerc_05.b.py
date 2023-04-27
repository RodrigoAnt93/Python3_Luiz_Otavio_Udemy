import json
with open('class_pokemon.json', 'r', encoding='utf8') as pokemon:
    dict_class_poke = json.load(pokemon)
print(dict_class_poke)


class Pokemon:
    def __init__(self, name, type):
        self.name = name
        self.type = type


squirtle = Pokemon(**dict_class_poke[1])
print(vars(squirtle))
print(squirtle.type)