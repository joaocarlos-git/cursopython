#Crie um programa para elaborar uma lista de convidados de uma festa,
# o programa ira perguntar o nome do convidado, você digitará o nome e ao
# terminar a lista, o pregorama irá exibir a lista em ordem alfabética.



convidados = []

print("Quando terminar digite FIM: \n")

while True:
    convidado = input("Digite o nome do convidado ou digite Fim: ")

    if convidado.lower() == "fim":
        break

    else:
        convidados.append(convidado.title())

convidados.sort()

print("\n###################Lista de Convidados #######################\n")

for convidado in convidados:
    print(">>>>>>>>>> " + convidado)