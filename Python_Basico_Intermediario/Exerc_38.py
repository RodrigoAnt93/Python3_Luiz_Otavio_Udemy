#alterar um atributo na pokedex.
from copy import deepcopy


def troca_atbt_base(dex, atbt, vl_nv):
    global pokemon
    pokemon[dex-1]['atbt_base'][atbt] = vl_nv


pokemon = [
    {1: 'Bulbasaur', "atbt_base": [45, 50, 50, 65, 65, 45]},
    {2: 'Ivysaur', 'atbt_base': [60, 62, 63, 80, 80, 60]},
    {3: 'Venusaur', 'atbt_base': [85, 85, 85, 100, 100, 80]},
    {4: 'Charmander', 'atbt_base': [45, 55, 45, 60, 50, 65]},
    {5: 'Charmeleon', 'atbt_base': [58, 64, 58, 80, 65, 80]},
    {6: 'Charizard', 'atbt_base': [78, 84, 78, 110, 85, 100]},
    {7: 'Squirtle', 'atbt_base': [49, 48, 65, 50, 65, 43]},
    {8: 'Wartortle', 'atbt_base': [64, 63, 80, 65, 75, 58]},
    {9: 'Blastoise', 'atbt_base': [85, 85, 100, 85, 100, 80]}
    ]

lista_temp = deepcopy(pokemon)
while True:
    lista_temp.clear()
    lista_temp = deepcopy(pokemon)
    for inx, poke in enumerate(lista_temp):
        print(f'N{inx+1}° - {poke[inx+1]} = (HP: {poke["atbt_base"][0]} - ATK: {poke["atbt_base"][1]} '
              f'- DEF: {poke["atbt_base"][2]} - SP.ATK: {poke["atbt_base"][3]} - SP.DEF: {poke["atbt_base"][4]}'
              f' - SPD: {poke["atbt_base"][5]})')
    print('')
    dex = int(input('N°: '))
    while True:
        atbt = int(input('HP = 0 - ATK = 1 - DEF = 2 - SP.ATK = 3 - SP.DEF = 4 - SPD = 5: '))
        if atbt >= 0 and atbt <= 5:
            break
        else:
            print('Opção Inválida')
            print('')

    vl_nv = int(input('Novo valor: '))
    print('')
    print('=-=' * 30)
    troca_atbt_base(dex, atbt, vl_nv)




