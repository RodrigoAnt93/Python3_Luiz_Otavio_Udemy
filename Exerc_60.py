#Criando o arquivo JSON para minha pokedex
import json

pokemon = [
    {"dex": 1, 'nome': 'Bulbasaur', "atbt_base": [45, 50, 50, 65, 65, 45], 'type': ['Planta', 'Venenoso']},
    {"dex": 2, 'nome': 'Ivysaur', 'atbt_base': [60, 62, 63, 80, 80, 60], 'type': ['Planta', 'Venenoso']},
    {"dex": 3, 'nome': 'Venusaur', 'atbt_base': [85, 85, 85, 100, 100, 80], 'type': ['Planta', 'Venenoso']},
    {"dex": 4, 'nome': 'Charmander', 'atbt_base': [45, 55, 45, 60, 50, 65], 'type': ['Fogo']},
    {"dex": 5, 'nome': 'Charmeleon', 'atbt_base': [58, 64, 58, 80, 65, 80], 'type': ['Fogo']},
    {"dex": 6, 'nome': 'Charizard', 'atbt_base': [78, 84, 78, 110, 85, 100], 'type': ['Fogo', 'Voador']},
    {"dex": 7, 'nome': 'Squirtle', 'atbt_base': [49, 48, 65, 50, 65, 43], 'type': ['Água']},
    {"dex": 8, 'nome': 'Wartortle', 'atbt_base': [64, 63, 80, 65, 75, 58], 'type': ['Água']},
    {"dex": 9, 'nome': 'Blastoise', 'atbt_base': [85, 85, 100, 85, 100, 80], 'type': ['Água']},
    {"dex": 10, "nome": "Caterpie", "atbt_base": [45, 30, 35, 20, 20, 20], "type": ["Inseto"]},
    ]

with open('Pokedex.json', 'w', encoding='utf8') as pokedex:
    json.dump(pokemon, pokedex)
