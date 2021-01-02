alimentos = ['Tomate', 'Batata', 'Uva', 'Banana', 'ovos', 'pao', 'pizza']

#pegando elementos da lista pega todos -1
print(alimentos[2:4])

#pegando elementos da lista pega todos -1
print(alimentos[:5])

#pegando elementos da lista com passo
print(alimentos[::2])

#pegando elementos da lista os três ultimos
print(alimentos[-3:])

#pegando elementos da lista usando for pega todos -1
for alimento in alimentos[:5]:
    print(alimento)