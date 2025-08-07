def CalculandoAMedia(lista):
    return sum(lista)/len(lista)
lista = [987654321,2,7654321,56,1234567, 1, 88888,3,42,999999,5,1000000000,13,101010,7,444, 9, 2, 13, 9]
Media = CalculandoAMedia(lista)
print(f'A média de {len(lista)} números em uma lista foi: {Media}')