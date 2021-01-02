lista_cor = ["vermelho", "verde", "preto", "branco", "azul"]
print(lista_cor)
def lista_funcao(lista):
    for cor in lista:
        print(cor)
        lista.pop()

lista_funcao(lista_cor[:])

print(lista_cor)