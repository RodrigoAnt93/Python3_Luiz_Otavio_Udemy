#Crie uma classe abstrata chamada "Ginásio" com atributos como nome, cidade e líder.
#Implemente um método abstrato chamado "desafiar_líder" que recebe um objeto "Treinador" e executa uma batalha entre os Pokemons do treinador e os do líder do ginásio.
#Crie pelo menos duas subclasses concretas da classe "Ginásio" com implementações diferentes do método "desafiar_líder".
from abc import ABC, abstractmethod
class Pokemon:
    def __init__(self, name, moves, type, lvl):
        self.name = name
        self.moves = moves
        self.type = type
        self.lvl = lvl


class  GYM(ABC):
    def __init__(self, name, city, leader, list_poke_leader):
        self.name = name
        self.city = city
        self.leader = leader
        self.list_poke_leader = list_poke_leader

    @abstractmethod
    def challenge_leader(self, list_poke_treiner):
        pass


class Brock(GYM):
    def __init__(self, name, city, leader, list_poke_leader):
        super().__init__(name, city, leader, list_poke_leader)

    def challenge_leader(self, list_poke_treiner):
        print(f'O pokemon {self.list_poke_leader[0]} do lider {self.name} VS {list_poke_treiner.list_pokemon[0]} do treinar {list_poke_treiner.name}')


class Treiner:
    def __init__(self, name, list_pokemon):
        self.name = name
        self.list_pokemon = list_pokemon


pewter_city = Brock('Brock', 'Pewter', 'Brock', ['Geodude', 'Onix'])
treiner = Treiner('Rodrigo', ['Charmander', 'Pidgeotto'])

pewter_city.challenge_leader(treiner)
