class Pokemon:
    def __init__(self, name, atbt_base, type, move, lvl):
        self.name = name
        self.atbt_base = atbt_base
        self.type = type
        self.move = move
        self.lvl = lvl


class Battler:
    def __init__(self, play_pokemon, wild_pokemon):
        self.play_pokemon = play_pokemon
        self.wild_pokemon = wild_pokemon

    def battle(self):
        from copy import deepcopy
        from random import randint
        from time import sleep
        pp = deepcopy(self.play_pokemon)
        pw = deepcopy(self.wild_pokemon)
        while True:
            print(f'Escolha um ataque do {pp.name}: ')
            for ind, move in pp.move.items():
                print(f'{ind}: {move[0]} = {move[1]}')
            while True:
                choice = int(input('Digite o numero do golpe: '))
                if choice <= len(pp.move):
                    break
                else:
                    print('Digite um numero válido.')
                    print()
            print(f'{pp.name} usou o ataque {pp.move[choice][0]}...'), sleep(1)
            damage = round((((2 * pp.lvl / 5 + 2) * pp.move[choice][1] * pp.atbt_base[1] / pw.atbt_base[2]) / 50 + 2))
            sleep(1)
            print(f'{pp.name} causou {damage} de dano em {pw.name}'), sleep(2)
            pw.atbt_base[0] -= damage
            if pw.atbt_base[0] <= 0:
                print(f'Fim da luta. {pp.name} venceu a luta')
                return
            else:
                pw_move = randint(1, len(pw.move))
                print(f'{pw.name} tem {pw.atbt_base[0]} de HP.'), sleep(2)
                damage = round((((2 * pw.lvl / 5 + 2) * pw.move[pw_move][1] * pw.atbt_base[1] / pp.atbt_base[2]) / 50 + 2))
                print(f'{pw.name} usou o ataque {pw.move[pw_move][0]}...'), sleep(2)
                print(f'{pw.name} causou {damage} de dano em {pp.name}'), sleep(2)
                pp.atbt_base[0] -= damage
                print(f'{pp.name} tem {pp.atbt_base[0]} de HP.'), sleep(2)
                if pp.atbt_base[0] <= 0:
                    print(f'Fim da luta. {pw.name} venceu a luta')
                    return
                print()