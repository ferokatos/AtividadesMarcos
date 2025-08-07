def RetornandoOMenorNumero(lista):
    for p,i in enumerate(lista):
        if p == 0:
            menor = i
        elif menor > i:
            menor = i
    return menor
lista = [987654321,2,7654321,56,1234567, 1, 88888,3,42,999999,5,1000000000,13,101010,7,444, 9, 2, 13, 9]
menorNumero = RetornandoOMenorNumero(lista)
print(f'O menor número encontrado foi: {menorNumero}')