def MaiorNumero(LST):
    for posicao,item in enumerate(LST):
        if posicao == 0:
            maior = item
        elif item > maior:
            maior = item
    return maior
maior = MaiorNumero([987654321,2,7654321,56,1234567, 1, 88888,3,42,999999,5,1000000000,13,101010,7,444, 9, 2, 13, 9])
print(f'O maior número encontrado foi: {maior}')