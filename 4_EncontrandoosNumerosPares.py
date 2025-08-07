def EncontrandoOsNumerosPares(LST):
    pares = []
    for i in LST:
        if i % 2 == 0:
            pares.append(i)
    return pares
pares = EncontrandoOsNumerosPares([987654321,2,7654321,56,1234567, 1, 88888,3,42,999999,5,1000000000,13,101010,7,444, 9, 2, 13, 9])
print(f'Os números pares retirados da lista foram: {pares}')