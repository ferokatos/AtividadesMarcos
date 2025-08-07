def JuntandoDuasListas(L1,L2):
    listaGeral = L1[:] + L2[:]
    return listaGeral
lista1 = ["rio", "floresta", "leão", "montanha", "oceano", "estrela", "vento", "cachoeira", "lua", "girassol"]
lista2 = ["algoritmo", "API", "blockchain", "código", "software", "nuvem", "hardware", "interface", "pixel", "servidor"]
lista_geral = JuntandoDuasListas(lista1,lista2)
print(f'A concatenação da lista1 + lista2 é igual a: {lista_geral}')