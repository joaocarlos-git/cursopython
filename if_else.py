carros = ["audi", "bmw", "ferrari", "honda"]

for carro in carros:
    if carro == "bmw":
        print(carro.upper())
    else:
        print(carro.title())
print("-"*50)

nome = input("Digite seu nome:  ")
idade = int(input("Digite sua idade: "))

# menor de 16 anos não vota
# entre 16 e 17 anos e acima de 65 anos voto opcional
# entre 18 e 65 anos obrigatório

if idade < 16:
    print(nome.upper() + ", você tem " + str(idade) + " anos e não pode votar.")

elif (idade >= 16 and idade <= 17) or (idade > 65):
    print(nome.upper() + ", você tem " + str(idade) + " anos e seu voto é opcional. ")

#elif idade > 65:
 #   print(nome.upper() + ", você tem " + str(idade) + " anos e seu voto é opcional. ")

#elif idade >= 18 and idade <= 65:
 #   print(nome.upper() + ", você tem " + str(idade) + " anos e seu voto é obrigatório")

else:
    print(nome.upper() + ", você tem " + str(idade) + " anos e seu voto é obrigatório")


print("-"*60)
 #============================================================
ingredientes = ["mostarda", "pimentão", "queijo extra"]
ingred_pedido = ["mostarda", "pimentão", "queijo extra", "tomate"]

for ingrediente in ingred_pedido:

    if ingrediente in ingredientes:
        print("Adicionando " + ingrediente + " a sua pizza. ")
        #print("Sinto muito, não temos pimentão. ")
    else:
        print("Sinto muito, não temos " + ingrediente + ".")
        #print("Adicionando " + ingrediente + " a sua pizza. ")

print("\nSua pizza está pronta. ")

print("-"*60)

#===================================================
#ingradientes pedidos pelo usuário
ingredientes = []
continuar = "s"

while continuar.lower() == "s":

    ing = input("Digite um ingrediente de sua preferencia: ")
    ingred_pedido.append(ing.lower())
    continuar = input("Deseja continuar? s ou n ")

#ingredientes da pizzaria
ingredientes = ["mostarda", "pimentão", "queijo extra"]

for ingrediente in ingred_pedido:

    if ingrediente in ingredientes:
        print("Adicionando " + ingrediente + " a sua pizza. ")
        #print("Sinto muito, não temos pimentão. ")
    else:
        print("Sinto muito, não temos " + ingrediente + ".")
        #print("Adicionando " + ingrediente + " a sua pizza. ")

print("\nSua pizza está pronta. ")

print("-"*60)
