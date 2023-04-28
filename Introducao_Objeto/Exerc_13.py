#Crie uma classe chamada Treinador com os seguintes atributos: nome, idade e lista_pokemon.
#A lista de Pokémon deve ser armazenada em uma lista.
#Crie um property para obter o número de Pokémon na lista e um setter para adicionar um novo Pokémon à lista.

class Trainer:
    def __init__(self, name, age, pokemon_list):
        self._name = name
        self._age = age
        self._pokemon_list = pokemon_list

    @property
    def pokemon_list(self):
        for ind, pokemon in enumerate(self._pokemon_list):
            print(f'{ind+1}° - {pokemon}')

    @pokemon_list.setter
    def pokemon_list(self, item_trade):
        del self._pokemon_list[item_trade[0] - 1]
        self._pokemon_list.insert(item_trade[0] - 1, item_trade[1])


trainer_Rodrigo = Trainer('Rodrigo', 29, ['Gengar', 'Charizard', 'Nidoking', 'Tangela', 'Seadra', 'Machamp'])
while True:
    trainer_Rodrigo.pokemon_list
    trade_poke = int(input('Digite a posição do pokemon que você quer trocar: '))
    new_poke = str(input('Digite o nome do novo pokemon: '))
    trainer_Rodrigo.pokemon_list = [trade_poke, new_poke]