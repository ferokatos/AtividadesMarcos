import os
limpa = lambda : os.system('cls')
def BuscandoUmNumero(LST,num):
    for i in LST:
        if i == num:
            return True
    return False
while True:
    try:
        num = (input("Digite um número para a procura('sair' para encerrar): "))
        if num.lower() == 'sair':
            break
        num = int(num)
        limpa()
        achou = BuscandoUmNumero([987654321,2,7654321,56,1234567, 1, 88888,3,42,999999,5,1000000000,13,101010,7,444, 9, 2, 13, 9,],num)
        if achou:
            print(f'o número {num} foi encontrado.')
        else:
            print(f'o número {num} não foi encontrado.')
    except ValueError:
        limpa()
        print('Digite algo válido.')

    
        