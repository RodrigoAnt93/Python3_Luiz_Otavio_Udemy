def posto_proximo(cbtv, kmL, posto):
    distancia_maxima = cbtv * kmL
    if distancia_maxima < posto[0]:
        return - 1
    else:
        for idx, pst in enumerate(posto):
            if distancia_maxima <= pst:
                return posto[idx - 1]


combustivel = 2
km_por_litro = 8
posto_gasolina = [2, 15, 22, 10.2]
posto_gasolina.sort()

print(posto_proximo(combustivel, km_por_litro, posto_gasolina))
