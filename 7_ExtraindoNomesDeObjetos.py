def ExtraindoNomesDeObjetos(DICT):
    nomes = []
    for i in DICT:
        for key,value in i.items():
            if key == 'nome':
                nomes.append(value)
    return nomes
dicionarios = [
    {"nome": "Carlos Lima",
    "idade": 35,
    "genero": "Masculino",
    "profissao": "Professor"},
    {"nome": "Ana Souza",
    "idade": 28,
    "genero": "Feminino",
    "profissao": "Engenheira de Software"},
    { "nome": "Mariana Silva",
    "idade": 22,
    "genero": "Feminino",
    "profissao": "Designer Gráfica"},
    {"nome": "João Pereira",
    "idade": 41,
    "genero": "Masculino",
    "profissao": "Médico"}
]
nomes = ExtraindoNomesDeObjetos(dicionarios)
print(f'Os nomes encontrandos na lista foram: ',end ='')
for posicao,nome in enumerate(nomes):
    if posicao == len(nomes) - 1:
        print(nome)
    elif posicao == len(nomes) - 2:
        print(f'{nome} e ',end='')
    else:
        print(f'{nome},',end='')