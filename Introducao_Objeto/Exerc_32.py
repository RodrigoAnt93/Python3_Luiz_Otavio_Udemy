#Crie uma classe decoradora que adicione uma mensagem de batalha antes e depois de uma função que simule uma batalha entre dois Pokemons.
class MessageBattle:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        print(f'A batalha vai começar!')
        print(self.func(*args, **kwargs))
        return f'Fim da batalha!'


@MessageBattle
def battle(poke_1, poke_2):
    return f'{poke_1} VS {poke_2}'


current_battle = battle('Gastly', 'Abra')
print(current_battle)