def calculadora_preco(tf1, vqr1, tf2, vqr2):
    tf1 = tf1
    vqr1 = vqr1
    tf2 = tf2
    vqr2 = vqr2
    gen = [g for g in range(1, 1000)]
    for conv in gen:
        emprsa_1 = tf1 + (vqr1 * conv)
        emprsa_2 = tf2 + (vqr2 * conv)
        if emprsa_1 == emprsa_2:
            if emprsa_1 < emprsa_2:
                return f'Se a corrida tiver {conv}km, tanto faz a empresa. Mas, se for menos que isso, a empresa_1 é mais barata.'
            else:
                return f'Se a corrida tiver {conv}km, tanto faz a empresa. Mas, se for menos que isso, a empresa_2 é mais barata.'


print(calculadora_preco(2.50, 1, 5, 0.75))
