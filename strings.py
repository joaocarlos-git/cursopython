nome1 = "joao"
nome2 = 'carlos'
# num = 5

nome_completo = " " + nome1 + " " + nome2
nome_completo = nome_completo.title()
# para ficar com a primeira letra do nome maiuscula
# nome_completo = nome_completo.title()

# para deixar todo maisusculo
# nome_completo = nome_completo.upper()

# converte para minusculo
# nome_completo = nome_completo.lower()
print("Olá " + nome_completo + ", Tudo bem?")
print("Olá " + nome_completo.lstrip() + ", Tudo bem?") #elimina espaço da esquerda
print("Olá " + nome_completo.rstrip() + ", Tudo bem?") #elimina espaço do lado direito
print("Olá " + nome_completo.strip() + ", Tudo bem?") #elimina todos os espaços desnecessarios

print("Olá " + nome_completo.strip() + ", tudo bem?\n Como vai a família?\n Manda um abraço!")

# print(nome1)
# print(nome2)


# concatenado dentro do print
# print("Ola " + nome_completo + "," + "tudo bem?")
# para concatenar de uma forma diferente
# print("Olá %s, %s, tudo bem?"%(nome_completo, nome2))
#concatenando com numeros
# print("Olá" + nome_completo + "," +str(num)+", tudo bem?")
