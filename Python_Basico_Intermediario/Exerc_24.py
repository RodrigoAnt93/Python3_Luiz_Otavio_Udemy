# Quiz Pokemon Red/Green com dicionários

perguntas = [
    {
        'pergunta': '1) Qual item é usado para acordar o Snorlax?',
        'opcoes': ('A) Stone', 'B) PokeFlauta', 'C) Rádio', 'D) Buzina'),
        'resposta': 'B'
    },
    {
        'pergunta': '2) Em qual cidade você ganha a MasterBall?',
        'opcoes': ('A) Saffron', 'B) Lavander', 'C) Cinnabar', 'D) Celadon'),
        'resposta': 'A'

    },
    {
        'pergunta': '3) Quando Kadabra evolui para um Alakazam?',
        'opcoes': ('A) lvl 30', 'B) lvl 35', 'C) Psy Stone', 'D) Trade'),
        'resposta': 'D'
    },
    {
        'pergunta': '4) Quais desses Pokemon o Brock usa em seu GYM?',
        'opcoes': ('A) Onix', 'B) Graveler', 'C) Rhydon', 'D) Marowak'),
        'resposta': 'A'
    },
    {
        'pergunta': '5) Em qual lvl o Charizard aprende o Flamethrower? ',
        'opcoes': ('A) lvl 36', 'B) lvl 40', 'C) lvl 46', 'D) lvl 45'),
        'resposta': 'C'
    },
    {
        'pergunta': '6) Qual lider de GYM você tem que derrotar para usar o HM Surf?',
        'opcoes': ('A) Lt. Surge', 'B) Misty', 'C) Koga', 'D) Sabrina '),
        'resposta': 'C'
    },
    {
        'pergunta': '7) Qual desses Pokemon \033[1;31mNÂO\033[m pode aprender o HM Fly?',
        'opcoes': ('A) Charizard', 'B) Golbat', 'C) Dodrio', 'D) Pidgey'),
        'resposta': 'B'
    },
    {
        'pergunta': '8) Onde encontrar o Pikachu?',
        'opcoes': ('A) Viridian Forest', 'B) Trade', 'C) Routes 5', 'D) Routes 22'),
        'resposta': 'A'
    },
    {
        'pergunta': '9) Qual o segundo tipo do Scyther?',
        'opcoes': ('A) Lutador', 'B) Não existe(Bug puro)', 'C) Sombrio', 'D) Voador'),
        'resposta': 'D'
    },
    {
        'pergunta': '10) Qual Pokemon é o N°55 na Pokedex?',
        'opcoes': ('A) Pikachu', 'B) Gengar', 'C) Golduck', 'D) Gloom'),
        'resposta': 'C'
    }


]
acertos = 0
for perg in perguntas:
    print(perg['pergunta'])
    for num, valor in enumerate(perg['opcoes']):
        print(valor)
    print('')
    while True:
        resp = input('Resposta: ').upper()[0]
        if resp not in 'ABCD':
            print('\033[1;31mOpção Inválida! Digite uma opção válida\033[m.')
        else:
            break
    if resp == perg['resposta']:
        acertos += 1
    print('=-=' * 15)
print('')
print(f'Você acertou \033[1;32m{acertos}\033[m respostas. Parabéns!' if acertos >= 6 else f'Você acertou \033[1;31m{acertos}\033[m respostas. Você tem que jogar mais =/')
