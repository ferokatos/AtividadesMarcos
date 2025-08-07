def ContandoOcorrencias(lista,num):
    return lista.count(num)
num = int(input('Digite um número para a procura: '))
contador = ContandoOcorrencias([987654321,2,7654321,56,1234567, 1, 88888,3,42,999999,5,1000000000,13,101010,7,444, 9, 2, 13, 9],num)
print(f'O número {num} aparece {contador} vezes')