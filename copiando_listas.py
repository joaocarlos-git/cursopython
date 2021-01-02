alimentos = ['Tomate', 'Batata', 'Uva', 'Banana', 'ovos', 'pao', 'pizza']


#copiando listas, assim quando altera uma lista não altera a outra
alimentos2 = alimentos[:]
#adicionando elementos na lista alimentos
alimentos.append('Hamburguer')
#jogando a lista de elementos de alimentos a alimentos2, assim quando adiciona em uma lista altera as duas
#alimentos2 = alimentos

#alterando a ordem dos elementos da lista
alimentos2.sort()

print(alimentos)
print(alimentos2)