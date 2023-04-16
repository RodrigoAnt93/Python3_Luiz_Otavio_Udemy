from math import ceil

assinante = [True, False, False, False, True, False, True, True, False, False, False]
minutos_assistidos = [6144, 2742, 330, 30, 1500, 4032, 24036, 3288, 2076, 24540, 4716]

cadastro_sorteio =[
    {'premium': a, 'minute': m, 'ticket': ceil(m/60)*2 if a else ceil(m/60)} for a, m in zip(assinante, minutos_assistidos)
]
chances = [
    round(c['ticket'] * 100 / sum(map(lambda v: v['ticket'], cadastro_sorteio)), 2) for c in cadastro_sorteio
]
print(*cadastro_sorteio, sep='\n')
print(chances)