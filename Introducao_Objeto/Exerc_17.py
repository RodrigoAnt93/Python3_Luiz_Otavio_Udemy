#Crie uma classe "Pokedex" com um atributo "pokemons" que é uma lista vazia.
#Implemente um método "adicionar_pokemon" na classe "Pokedex" que adiciona um objeto "Pokemon" à lista "pokemons".
#Crie uma classe "Treinador" com atributos como nome, idade, cidade e uma referência à Pokedex do treinador.
#Associe a classe "Pokedex" à classe "Treinador" para que cada treinador tenha uma Pokedex com seus Pokémons.
class Pokedex:
    def __init__(self):
        self.pokedex = []

    def add_pokemon(self, data_poke):
        self.pokedex.append(data_poke)

    def pokedex_list(self):
        for pokemon in self.pokedex:
            print(pokemon)

class Treiner:
    def __init__(self, name, age, city):
        self.name = name
        self.age = age
        self.city = city
        self.t_pokedex = Pokedex()

    def new_poke_seen(self, data_poke):
        self.t_pokedex.add_pokemon(data_poke)


class Pokemon:
    def __init__(self, name, type, lvl):
        self.name = name
        self.type = type
        self.lvl = lvl
        self.data_pokedex = vars(self)


trainer = Treiner('Rodrigo', 29, 'Pallet')
gastly = Pokemon('Gastly', ['Ghost', 'Poison'], 25)
charmander = Pokemon('Charmander', ['Fire'], 14)
ratatta = Pokemon('Ratatta', ['Normal'], 5)

trainer.new_poke_seen(gastly.data_pokedex)
trainer.new_poke_seen(charmander.data_pokedex)
trainer.new_poke_seen(ratatta.data_pokedex)

trainer.t_pokedex.pokedex_list()