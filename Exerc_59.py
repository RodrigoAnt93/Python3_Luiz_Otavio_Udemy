musicas_tocadas = [2, 10, 5, 3, 8, 7]
copy_MT = sorted(musicas_tocadas.copy())
lista_mista = []
troca = 0
for c in range(len(copy_MT)):
    if troca == 0:
        lista_mista.append(copy_MT.pop(-1))
        troca = 1
    else:
        lista_mista.append(copy_MT.pop(0))
        troca = 0
print(lista_mista)

