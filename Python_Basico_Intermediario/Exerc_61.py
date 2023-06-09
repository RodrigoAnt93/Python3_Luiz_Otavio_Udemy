#Criando código para alimentar minha pokedex e salvar usando JSON
import json

with open('Pokedex.json', 'r', encoding='utf8') as pokedex:
    pokemon = json.load(pokedex)
    while True:
        print(f'O último pokemon cadastrado foi o {pokemon[-1]["dex"]}° {pokemon[-1]["nome"]}.')
        print()
        nome_poke = str(input('Qual o nome do Pokemon? ')).title().strip()
        print('Precisamos dos atributos do pokemon agora:')
        atributos = []
        atributos.append(int(input('HP: ')))
        atributos.append(int(input('ATK: ')))
        atributos.append(int(input('DEF: ')))
        atributos.append(int(input('SP.ATK: ')))
        atributos.append(int(input('SP.DEF: ')))
        atributos.append(int(input('SPD: ')))
        print("•" * 15)
        type_poke = []
        quant_tipo = int(input('Quantos tipos tem o pokemon? '))
        for c in range(quant_tipo):
            type_poke.append(str(input(f'Qual {c + 1}° tipo? ')).title())
        print("•" * 15)
        print(f'Revisão: O nome do Pokemon é {nome_poke} e os atributos são {atributos}. O tipo dele é {type_poke}')
        while True:
            opc = str(input('Deseja continuar? [S/N] ')).upper()[0]
            if opc == 'S' or opc == 'N':
                break
            else:
                print("Responda 'S' ou 'N'!")
        if opc == 'S':
            pokemon.append({"dex": (pokemon[-1]["dex"] + 1), "nome": nome_poke, 'atbt_base': atributos, "type": type_poke})
            with open('Pokedex.json', 'w', encoding='utf8') as pokedex:
                json.dump(pokemon, pokedex, indent=2, ensure_ascii=False)
            print('Pokemon Cadastrado!')
        else:
            print('Cadastro Cancelado"')
        while True:
            opc_2 = str(input('Deseja cadastrar novamente? ')).upper()[0]
            if opc_2 == 'S' or opc_2 == 'N':
                break
            else:
                print("Responda 'S' ou 'N'!")
        if opc_2 == 'N':
            break
        print()

