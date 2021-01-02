carros = ['ferrari', 'fusca', 'civic']

print(carros[2].title()) #imprime a primeira letra maiuscula
print("Eu gostaria de ter uma " + carros[-1].title()) #imprime o ultimo elemento da lista
print("Eu 'gostaria' de ter uma " + carros[-1].title()) #aspas simples e aspas duplas para reconhecer como string


carros[1] = 'mustang'# trocando o fusca pelo mustang
print(carros)

carros.append('BMW') #adicionando um elemento no final da lista
print(carros)

carros.insert(1,'jeep') #adicionando o elemento jeep na posição 1 da lista
print(carros)

carros.extend('fusca') #adicionando o fusca na lista, so q com essa função ele adiciona cada letra como uma string
print(carros)

del carros[1]#removendo elementos da lista no caso 1
print(carros)

carros.pop()#removendo o ultino elemento da lista
print(carros)

carros.pop(2) #removendo o  elemento 2 da lista
print(carros)

carros.remove('mustang') #remove o elemento pelo nome e não pela posição
print(carros)

carros.sort() #organiza a lista por ordem alfabetica de a a z
print(carros)

carros.sort(reverse=True) #organiza a lista por ordem alfabetica inversa
print(carros)

print(sorted(carros))#ordenando a lista dentro do print de a a z

print(len(carros)) # traz a lista e quantidade de elementos tem na lista

carros.reverse()#inverte a posição dos elementos da lista
print(carros)