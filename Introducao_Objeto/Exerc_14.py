#Crie uma classe chamada Pokedex com os seguintes atributos: lista_pokemon e pokemon_atual.
#A lista de Pokémon deve ser armazenada em uma lista e o Pokémon atual deve ser armazenado como um objeto da classe Pokemon.
#Crie um property para obter o nome do Pokémon atual e um setter para definir o Pokémon atual a partir da lista.

class Pokemon:
    def __init__(self, name):
        self.name = name


class Pokedex:
    def __init__(self, pokemon_list):
        self._pokemon_list = pokemon_list
        self._actual_pokemon = Pokemon(self._pokemon_list[0])

    @property
    def pokemon_list(self):
        for ind, pokemon in enumerate(self._pokemon_list):
            print(f'{ind+1}° - {pokemon}')
        return

    @property
    def actual_pokemon(self):
        return self._actual_pokemon

    @actual_pokemon.setter
    def actual_pokemon(self, trade):
        self._actual_pokemon = Pokemon(self._pokemon_list[(trade - 1)])


treiner = Pokedex(['Gengar', 'Charizard', 'Nidoking', 'Tangela', 'Seadra', 'Machamp'])
while True:
    treiner.pokemon_list
    print(f'O pokemon atual é {treiner.actual_pokemon.name}.')
    opt = int(input('Digite o número do pokemon que você quer trocar: '))
    treiner.actual_pokemon = opt