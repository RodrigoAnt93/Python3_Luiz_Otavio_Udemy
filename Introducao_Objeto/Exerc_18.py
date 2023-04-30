#Crie uma classe "Ataque" com atributos como nome, tipo e força.
#Crie uma classe "Pokemon" com atributos como nome, tipo e nível, e uma lista de objetos "Ataque".
#Implemente um método "adicionar_ataque" na classe "Pokemon" que adiciona um objeto "Ataque" à lista de ataques.
#Crie uma classe "Treinador" com atributos como nome, idade, cidade e uma lista de objetos "Pokemon".
#Associe a classe "Pokemon" à classe "Treinador" para que cada treinador tenha um ou mais Pokémons compostos por uma lista de ataques.
class Move:
    def __init__(self, name, power, type):
        self.name = name
        self.power = power
        self.type = type

    def move(self):
        return vars(self)


class Pokemon:
    def __init__(self, name, type, lvl):
        self.name = name
        self.type = type
        self.lvl = lvl
        self.moves = []

    def learn_new_move(self, move):
        if len(self.moves) == 4:
            print(f'O {self.name} já aprendeu 4 golpes. Você precisa excluir um golpe para aprender o {move.name}')
            for ind, m in enumerate(self.moves):
                print(f'{ind+1} = {m.name}')
            choice = int(input('Digite o numero do golpe que deseja apagar: '))
            del self.moves[choice-1]
            self.moves.insert(choice-1, move)
        else:
            self.moves.append(move)

    def list_move(self):
        for ind, m in enumerate(self.moves):
            print(f'{ind + 1} = {m.name}')


lick = Move('Lick', 30, ['Ghost', 'Physical'])
confuse_ray = Move('Confuse Ray', None, ['Ghost'])
hypnosis = Move('Hypnosis', None, ['Physical'])
mean_look = Move('Mean Look', None, ['Normal'])
payback = Move('Payback', 50, ['Dark', 'Physical'])
gastly = Pokemon('Gastly', ['Ghost', 'Poison'], 25)
while True:
    gastly.learn_new_move(lick)
    gastly.learn_new_move(confuse_ray)
    gastly.learn_new_move(hypnosis)
    gastly.learn_new_move(mean_look)
    gastly.learn_new_move(payback)
    gastly.list_move()
    stop = input('continuar?')
