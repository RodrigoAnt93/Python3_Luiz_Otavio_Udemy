#Crie uma classe "Treinador" com atributos como nome, idade e cidade.
#Crie uma classe "Pokemon" com atributos como nome, tipo e nível.
#Associe a classe "Pokemon" à classe "Treinador" para que cada treinador tenha um ou mais Pokémons associados.
class Treiner:
    def __init__(self, name, age, city):
        self.name = name
        self.age = age
        self.city = city
        self._pokemon = []

    @property
    def pokemon_list(self):
        return self._pokemon

    @pokemon_list.setter
    def pokemon_list(self, new_pokemon):
        self._pokemon.append(new_pokemon)


class Pokemon:
    def __init__(self, name, type, lvl):
        self.name = name
        self.type = type
        self.lvl = lvl

    def attack(self):
        return f'{self.name} está atacando!'


trainer = Treiner('Rodrigo', 29, 'Pallet')
gastly = Pokemon('Gastly', ['Ghost', 'Poison'], 25)
charmander = Pokemon('Charmander', ['Fire'], 14)
trainer.pokemon_list = gastly
trainer.pokemon_list = charmander
print(trainer.pokemon_list[0].attack())
print(trainer.pokemon_list[1].attack())