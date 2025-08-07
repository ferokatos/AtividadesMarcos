def VerificandoSeAListaEstaVazia(lista):
    if not lista:
        return True
    else:
        return False
lista = []
print(f'A lista é vazia? {VerificandoSeAListaEstaVazia(lista)}')