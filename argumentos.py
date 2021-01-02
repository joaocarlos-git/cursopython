def animais(especie, nome):
    especie = especie
    nome = nome

    print("Eu tenho um " + especie + " chamado " + nome)

#animais('cachorro', 'Aquiles')
#animais('gato', 'Cokei')

#passando argumentos invertidos mas nomeando
animais(nome="Aquiles", especie="cachorro")

print('-'*80)
def animais(especie = "cachorro", nome=""):
    especie = especie
    nome = nome

    print("Eu tenho um " + especie + " chamado " + nome)

#animais('cachorro', 'Aquiles')
#animais('gato', 'Cokei')

#passando argumentos invertidos mas nomeando
#animais(nome="Aquiles", especie="cachorro")
animais(nome="Aquiles")
animais(especie="gato", nome="Bichano")

print('-'*80)

def nome_completo(primeiro_nome="", ultimo_nome = "", nome_do_meio=""):
    primeiro_nome = primeiro_nome
    ultimo_nome = ultimo_nome
    nome_do_meio = nome_do_meio

    if nome_do_meio != "":
        print("O nome digitado foi " + primeiro_nome.title() +" " + nome_do_meio.title() +" " + ultimo_nome.title())
    else:
        print("O nome digitado foi " + primeiro_nome.title() +" "+ ultimo_nome.title())
nome_completo("joao","ribeiro","Carlos",)
nome_completo("joao","Carlos",)


