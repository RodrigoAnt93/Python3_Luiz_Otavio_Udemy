#Jogo da forca.

while True:
    chance = 5

    letra_acertada = ''
    palavra = input('Digite uma palavra: ').lower()
    for i in range(15):# O FOR foi usado para tirar a palavra digitada da tela com os pontos subindo o cursor.
        print('.')
    print(f'A palavra foi salva:', '*' * len(palavra))
    while chance > 0:
        letra = input('Digite uma letra para a forca: ').lower()
        if len(letra) == 1:
            pass
        else:
            print('Digite apenas uma única letra!')
            print('')
            continue
        if letra in palavra:
            letra_acertada += letra
        else:
            chance -= 1
            print(f'\033[1;33mVocê errou. Você ainda tem {chance} chances\033[m')
        palavra_secreta = ''
        for letra_secret in palavra:
            if letra_secret in letra_acertada:
                palavra_secreta += letra_secret
            else:
                palavra_secreta += '*'


        print(f'{palavra_secreta}')

        if '*' not in palavra_secreta:
            print('\033[1;32mParabéns! Você acertou a palavra secreta!\033[m')
            print('')
            break

        if chance == 0:
            print('\033[1;31mVocê perdeu! Você usou todas suas chances e não acertou a palavra secreta\033[m')
            print('')
            break




