def SegundoMaiorNumero(LST):
    for posicao,item in enumerate(LST):
        if posicao == 0:
            maior = item
        elif item > maior:
            maior = item
    LST.remove(maior)
    for posicao,item in enumerate(LST):
        if posicao == 0:
            SegundoMaior = item
        elif SegundoMaior < item:
            SegundoMaior = item
    return SegundoMaior
SegundoMaior = SegundoMaiorNumero([987654321,2,7654321,56,1234567, 1, 88888,3,42,999999,5,1000000000,13,101010,7,444, 9, 2, 13, 9])
print(f'O segundo maior número encontrado foi: {SegundoMaior}')


